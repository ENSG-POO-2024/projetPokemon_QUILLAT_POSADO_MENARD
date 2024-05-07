## Partie qui créée les pokémons, le pokedex et permet de créer l'inventaire du joueur


####### Bibliothèques #######
from math import *
import numpy as np
import pandas as pd
import os
from abc import *


####### Code #######

class Pokemon:
    def __init__(self, name, x, y, hp, attack, defense, sp_attack, sp_defense, type_, sauvage_):
        self.name = name
        self.x = x
        self.y = y
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.type = type_ #pour eviter le type de python on met type_
        self.sauvage = sauvage_ 

    @classmethod
    def creer_pokemon(cls, name, x, y, hp, attack, defense, sp_attack, sp_defense, type_, sauvage):
        return cls(name, x, y, hp, attack, defense, sp_attack, sp_defense, type_, sauvage)

    # def attaquer(self, other_pokemon):
    #     print(f"{other_pokemon.name} a {other_pokemon.hp} hp et {other_pokemon.defense} point de defense et {self.name} a {self.attack} point d'attaque.")
    #     new_att = self.new_attack(other_pokemon.type)
    #     degats = new_att - other_pokemon.defense 
    #     other_pokemon.hp -= degats
    #     print(f"{self.name} attaque {other_pokemon.name} et lui inflige {degats} dégâts.")
    #     print(f"Il reste {other_pokemon.hp} point de vie à {other_pokemon.name}")

    def modifier(self, type_adversaire):
        if type_adversaire.name in self.type.fort:
            return 2
        elif type_adversaire.name in self.type.faible:
            return 0.5
        elif type_adversaire.name in self.type.neutre:
            return 0
        else:
            return 1
        
    def attaquer(self, adversaire):
        degats = self.attack * self.modifier(adversaire.type) - adversaire.defense
        adversaire.hp -= degats
        if adversaire.hp < 0:
                adversaire.hp = 0
        print(f"{self.name} attaque {adversaire.name} et lui inflige {degats} dégâts.")
        print(f"Il reste {adversaire.hp} points de vie à {adversaire.name}.")

    def attaque_speciale_joueur(self, adversaire, tour_avant_attaque_speciale):
        # Vérifie si l'attaque spéciale est disponible
        if tour_avant_attaque_speciale == 0:
            # Utilise l'attaque spéciale
            degats = self.sp_attack * self.modifier(adversaire.type) - adversaire.sp_defense
            adversaire.hp -= degats  
            if adversaire.hp < 0:
                adversaire.hp = 0
            print(f"{self.name} utilise son attaque spéciale sur {adversaire.name} et lui inflige {degats} dégâts.")
            print(f"Il reste {adversaire.hp} points de vie à {adversaire.name}.")
            # Réinitialise le compteur de tours avant la prochaine attaque spéciale
            tour_avant_attaque_speciale = 2
        else:
            print("L'attaque spéciale n'est pas encore disponible.")
        

        

class Type(Pokemon):
    def __init__(self, name, fort=[], faible=[], neutre=[]):
        super().__init__(name, None, None, None, None, None, None, None, None, None)
        self.fort = fort
        self.faible = faible
        self.neutre = neutre

class Acier(Type):
     def __init__(self):
        super().__init__("Acier", fort=["Fee", "Glace", "Roche"], faible=["Acier", "Eau", "Feu", "Electrik"], neutre=[])


class Combat(Type):
     def __init__(self):
        super().__init__("Combat", fort=["Acier", "Glace", "Normal", "Tenebres", "Roche"], faible=["Fee", "Insecte", "Poison", "Psy", "Vol"], neutre=["Spectre"])


class Dragon(Type):
     def __init__(self):
        super().__init__("Dragon", fort=["Dragon"], faible=["Acier"], neutre=["Fee"])


class Eau(Type):
     def __init__(self):
        super().__init__("Eau", fort=["Feu", "Sol", "Roche"], faible=["Dragon", "Eau", "Plante"], neutre=[])


class Electrik(Type):
     def __init__(self):
        super().__init__("Electrik", fort=["Eau", "Vol"], faible=["Dragon", "Electrik", "Plante"], neutre=[])


class Feu(Type):
     def __init__(self):
        super().__init__("Feu", fort=["Acier", "Glace", "Insecte", "Plante"], faible=["Dragon", "Eau", "Feu", "Roche"], neutre=[])


class Fee(Type):
     def __init__(self):
        super().__init__("Fee", fort=["Combat", "Dragon", "Tenebres"], faible=["Acier", "Feu", "Poison"], neutre=[])


class Glace(Type):
     def __init__(self):
        super().__init__("Glace", fort=["Dragon", "Vol", "Plante", "Sol"], faible=["Acier", "Eau", "Feu", "Glace"], neutre=[])


class Insecte(Type):
     def __init__(self):
        super().__init__("Insecte", fort=["Plante", "Psy", "Tenebres"], faible=["Acier", "Combat", "Feu", "Fee", "Poison", "Spectre", "Vol"], neutre=[])


class Normal(Type):
     def __init__(self):
        super().__init__("Normal", fort=[], faible=["Acier", "Roche"], neutre=["Spectre"])


class Plante(Type):
     def __init__(self):
        super().__init__("Plante", fort=["Eau", "Roche", "Sol"], faible=["Acier", "Dragon", "Feu", "Insecte", "Plante", "Poison", "Vol"], neutre=[])


class Poison(Type):
     def __init__(self):
        super().__init__("Poison", fort=["Fee", "Plante"], faible=["Poison", "Roche", "Sol", "Spectre"], neutre=["Acier"])


class Psy(Type):
     def __init__(self):
        super().__init__("Psy", fort=["Combat", "Poison"], faible=["Acier", "Psy"], neutre=["Tenebres"])


class Roche(Type):
     def __init__(self):
        super().__init__("Roche", fort=["Feu", "Glace", "Insecte", "Vol"], faible=["Acier", "Combat", "Sol"], neutre=[])


class Sol(Type):
     def __init__(self):
        super().__init__("Sol", fort=["Acier", "Feu", "Electrik", "Poison", "Roche"], faible=["Insecte", "Plante"], neutre=["Vol"])


class Spectre(Type):
     def __init__(self):
        super().__init__("Spectre", fort=["Psy", "Spectre"], faible=["Tenebres"], neutre=["Normal"])


class Tenebres(Type):
     def __init__(self):
        super().__init__("Tenebres", fort=["Psy", "Spectre"], faible=["Combat", "Fee", "Tenebres"], neutre=[])


class Vol(Type):
     def __init__(self):
        super().__init__("Vol", fort=["Combat", "Insecte", "Plante"], faible=["Acier", "Electrik", "Roche"], neutre=[])



# # Création des Pokémon avec leurs types respectifs et des statistiques personnalisées
# magicarpe = Pokemon.creer_pokemon("Magicarpe", 50, 20, 10, 35, 15, Eau())
# charmander = Pokemon.creer_pokemon("Charmander", 70, 25, 15, 35, 25, Feu())
# pikachu = Pokemon.creer_pokemon("Pikachu", 60, 30, 12, 40, 20, Electrik())

# # Combat entre Pikachu et Magicarpe
# pikachu.attaquer(magicarpe)


class Pokedex:
    def __init__(self):
        self.pokedex = {}

    def charger_pokedex(self, fichier):
        # On prend le chemin du répertoire parent du script Python
        chemin_parent = os.path.dirname(os.path.abspath(__file__))
        # On construit le chemin complet du fichier CSV en joignant le chemin du répertoire parent avec le répertoire "data" et le nom du fichier
        chemin_fichier = os.path.join(chemin_parent, 'data', fichier)
        # On charge le fichier CSV en tant que DataFrame avec Pandas
        data = pd.read_csv(chemin_fichier)
        for index, row in data.iterrows():
            name = row['Name']  
            x = row['X']
            y = row['Y']
            hp = row['HP']
            attack = row['Attack']
            defense = row['Defense']
            sp_attack = row['Sp. Atk']
            sp_defense = row['Sp. Def']
            type_name = row['Type 1'] 
            type_obj = globals()[type_name]()
            sauvage = False
            pokemon = Pokemon(name, x, y, hp, attack, defense, sp_attack, sp_defense, type_obj, sauvage)
            # On ajoute les Pokémons au dictionnaire avec leur nom comme clé
            self.pokedex[name] = pokemon

    def afficher_pokedex(self):
        for nom_pokemon, pokemon in self.pokedex.items():
            print(f"Nom: {pokemon.name}")
            print(f"X: {pokemon.x}")
            print(f"Y: {pokemon.y}")
            print(f"HP: {pokemon.hp}")
            print(f"Attaque: {pokemon.attack}")
            print(f"Défense: {pokemon.defense}")
            print(f"Sp. Attaque: {pokemon.sp_attack}")
            print(f"Sp. Défense: {pokemon.sp_defense}")
            print(f"Type: {pokemon.type.name}")
            print(f"Sauvage: {pokemon.sauvage}")
            print()  # Ajouter une ligne vide entre chaque Pokémon
        return 

class InventaireJoueur(Pokedex):
    def __init__(self):
        super().__init__()
        self.inventaire_joueur = {}

    def inventory(self, pokemon): 
        if pokemon.name not in self.pokedex:
            # Si le nom du Pokémon n'existe pas dans l'inventaire du joueur, on l'ajoute directement
            self.pokedex[pokemon.name] = pokemon
        else:
            # Si le nom du Pokémon existe déjà, on trouve le prochain numéro de séquence disponible 
            # pour que deux pokémons n'aient pas le même nom
            sequence = 2
            new_name = f"{pokemon.name} {sequence}" # On travaille avec un dictionnaire donc on doit gérer les clés et en créé une nouvelle
            while new_name in self.pokedex:
                sequence += 1
                new_name = f"{pokemon.name} {sequence}"
            # On crée une copie du Pokémon avec le nom modifié pour éviter d'écraser la précédente clé
            pokemon_copie = Pokemon(new_name, pokemon.x, pokemon.y, pokemon.hp, pokemon.attack, pokemon.defense, pokemon.sp_attack, pokemon.sp_defense, pokemon.type, pokemon.sauvage)
            # On ajoute le Pokémon avec le nom modifié à l'inventaire du joueur
            self.pokedex[new_name] = pokemon_copie
        
        pokemon.x = None # Le pokemon est maintenant dans notre inventaire
        pokemon.y = None # il n'a plus de coordonnées

    # def afficher_equipe(self, equipe):
    #     print("Équipe du joueur :\n")
    #     for nom_pokemon, pokemon in equipe.items():
    #         print(f"Nom: {pokemon.name}")
    #         print(f"HP: {pokemon.hp}")
    #         print(f"Attaque: {pokemon.attack}")
    #         print(f"Défense: {pokemon.defense}")
    #         print(f"Sp. Attaque: {pokemon.sp_attack}")
    #         print(f"Sp. Défense: {pokemon.sp_defense}")
    #         print(f"Type: {pokemon.type.name}")
    #         print(f"Sauvage: {pokemon.sauvage}")
    #         print()  # Ajouter une ligne vide entre chaque Pokémon


    # def poke_sauvage(self, fichier):
    #     pokemons_sauvages = InventaireJoueur()
    #     # On prend le chemin du répertoire parent du script Python
    #     chemin_parent = os.path.dirname(os.path.abspath(__file__))
    #     # On construit le chemin complet du fichier CSV en joignant le chemin du répertoire parent avec le répertoire "data" et le nom du fichier
    #     chemin_fichier = os.path.join(chemin_parent, 'data', fichier)
    #     # On charge le fichier CSV en tant que DataFrame avec Pandas
    #     data = pd.read_csv(chemin_fichier)
    #     for index, row in data.iterrows():
    #         name = row['Name']  
    #         x = row['X']
    #         y = row['Y']
    #         hp = row['HP']
    #         attack = row['Attack']
    #         defense = row['Defense']
    #         sp_attack = row['Sp. Atk']
    #         sp_defense = row['Sp. Def']
    #         type_name = row['Type 1'] 
    #         type_obj = globals()[type_name]()
    #         sauvage = False
    #         pokemon = Pokemon(name, x, y, hp, attack, defense, sp_attack, sp_defense, type_obj, sauvage)
    #         # On ajoute les Pokémons au dictionnaire avec leur nom comme clé
    #         pokemons_sauvages.inventory(pokemon)
            
    #     return pokemons_sauvages



    def creer_equipe(self):
        equipe = InventaireJoueur()
        pokemons_disponibles = list(self.pokedex.keys()) # Liste des noms de tous les pokémons disponibles
        for _ in range(3):  # Sélectionner 3 pokémons pour former l'équipe
            if not pokemons_disponibles:  # Si l'inventaire est vide
                break
            pokemon_choisi = input("Choisissez un Pokémon pour rejoindre votre équipe : ")
            while pokemon_choisi not in pokemons_disponibles:
                print("Ce Pokémon n'est pas dans votre inventaire. Veuillez choisir un autre Pokémon.")
                pokemon_choisi = input("Choisissez un Pokémon pour rejoindre votre équipe : ")
            equipe.inventory(self.pokedex[pokemon_choisi]) 
            pokemons_disponibles.remove(pokemon_choisi)  # Retirer le pokémon choisi de la liste des pokémons disponibles

        self.afficher_pokedex()

        return equipe
    



if __name__ == '__main__':
    # Exemple d'utilisation
    pokedex = Pokedex()
    inventaire_joueur = InventaireJoueur()
    magicarpe = Pokemon.creer_pokemon("Magicarpe", 0, 0, 50, 20, 10, 35, 15, Eau(), False)
    pokedex.charger_pokedex('pokemon_first_gen.csv')
    pokedex.afficher_pokedex()
    inventaire_joueur.inventory(magicarpe)
    # inventaire_joueur.inventory(magicarpe)
    # inventaire_joueur.afficher_pokedex()
    # inventaire_joueur.creer_equipe()




    # # On charge le Pokédex à partir du fichier CSV
    # pokedex = charger_pokedex('pokemon_first_gen.csv')


    # # Afficher le Pokédex
    # #afficher_dico(pokedex)


    # # Nom du Pokémon à tester
    # nom_pokemon_test = "Salamèche"  # Remplacez "Bulbasaur" par le nom du Pokémon que vous voulez tester

    # # # Vérifier si le Pokémon est dans le Pokédex
    # # if nom_pokemon_test in pokedex:
    # #     print(f"Le Pokémon '{nom_pokemon_test}' est présent dans le Pokédex.")
    # # else:
    # #     print(f"Le Pokémon '{nom_pokemon_test}' n'est pas présent dans le Pokédex.")


