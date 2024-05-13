## Partie qui gère les combats

####### Bibliothèques #######
from math import *
import numpy as np
import pandas as pd
import os
from abc import *
import Poke as poke  # Importer les classes nécessaires depuis Pokemon.py
import Combat.CombatVis3u as c 

####### Code #######

class Combat:
    def __init__(self, equipe_joueur, pokemon_adverse):
        self.equipe_joueur = equipe_joueur
        self.pokemon_adverse = pokemon_adverse
        self.pokemon_utilise = None  # Le Pokémon actuellement utilisé par le joueur
        self.tour_joueur = True  # Indique si c'est le tour du joueur
        self.tour_avant_attaque_speciale = 0  # Nombre de tours depuis la dernière attaque spéciale


    def changer_pokemon(self, pokemon_a_envoyer, pokemon_a_recevoir):
        print(f"Le joueur change {pokemon_a_envoyer.name} pour {pokemon_a_recevoir.name}")
        self.pokemon_utilise = pokemon_a_recevoir
        print(f"Pokémon utilisé : {self.pokemon_utilise.name}")


    def commencer_combat(self):
        print("Le combat commence !")
        print(f"Pokémon adverse : {self.pokemon_adverse.name}, HP: {self.pokemon_adverse.hp}, att: {self.pokemon_adverse.attack}, def: {self.pokemon_adverse.defense}")

        # Sélection du premier Pokémon de l'équipe du joueur
        self.pokemon_utilise = list(self.equipe_joueur.pokedex.values())[0]

        while self.pokemon_utilise.hp > 0 and self.pokemon_adverse.hp > 0:
            if self.tour_joueur:
                action = input("Choisissez une action : attaquer (A) ou attaque spéciale (S) ou changer de Pokémon (C) : ").upper()
                while action != "A" and action != "S" and action != "C":
                    print("Action non valide.")
                    action = input("Choisissez une action : attaquer (A) ou attaque spéciale (S) ou changer de Pokémon (C) : ").upper()
                
                if action == "A":
                    self.pokemon_utilise.attaquer(self.pokemon_adverse)
                    self.tour_avant_attaque_speciale -= 1
                elif action == "S":
                    self.pokemon_utilise.attaque_speciale_joueur(self.pokemon_adverse, self.tour_avant_attaque_speciale)
                elif action == "C":
                    print(f"Vous allez changer {self.pokemon_utilise.name}")
                    pokemon_a_recevoir = input("Choisissez le Pokémon à recevoir : ")
                    self.changer_pokemon(self.pokemon_utilise, self.equipe_joueur.pokedex[pokemon_a_recevoir])
                self.tour_joueur = False
            
            else:
                self.pokemon_adverse.attaquer(self.pokemon_utilise)
                self.tour_joueur = True
            
            # Vérifie si le Pokémon utilisé par le joueur a été vaincu
            if self.pokemon_utilise.hp <= 0:
                # Cherche le prochain Pokémon de l'équipe du joueur qui est en vie
                for pokemon in self.equipe_joueur.pokedex.values():
                    if pokemon.hp > 0:
                        print(f"{pokemon.name} n'a plus de point de vie. ")
                        self.pokemon_utilise = pokemon
                        print(f"Pokémon utilisé : {self.pokemon_utilise.name}")
                        break
                else:
                    print("Dommage vous avez perdu.")
                    break
        
        if self.pokemon_adverse.hp <= 0:
            print("\nGG !\n")
            self.equipe_joueur.inventory(self.pokemon_adverse)
            self.equipe_joueur.afficher_pokedex()
            
         


# Exemple d'utilisation :
if __name__ == "__main__":
    # Création d'une équipe de joueur
    joueur = poke.InventaireJoueur()
    magicarpe = poke.Pokemon.creer_pokemon("Magicarpe", 0, 0, 50, 60, 10, 35, 15, poke.Eau(), False)
    florizard = poke.Pokemon.creer_pokemon("Fleurizard",0, 0, 50, 45, 10, 35, 15, poke.Plante(), False)
    joueur.inventory(magicarpe)
    joueur.inventory(florizard)
    equipe_joueur = joueur.creer_equipe()

    # Création d'un Pokémon adverse
    pokemon_adverse = poke.Pokemon("Pika", 100, 30, 20, 25, 25, poke.Feu(), False)

    # Création d'une instance de Combat
    combat = Combat(equipe_joueur, pokemon_adverse)
    combat.commencer_combat()