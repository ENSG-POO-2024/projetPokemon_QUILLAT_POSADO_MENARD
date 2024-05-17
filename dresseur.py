
import numpy as np


class Dresseur:

    SIZE = 10
    DISTANCE_COMBAT = 3
    DISTANCE_AFFICHAGE = 312 # Affiche les pokémons dans un carré de 3 blocs
    VITESSE_DEPART = 110
    
    def __init__(self, x, y, X, Y, sacha):
        self.x = x # x d'affichage
        self.y = y # x d'affichage
        self.X = X # X de coordonnées
        self.Y = Y # Y de coordonnées
        self.speed = self.VITESSE_DEPART # Vitesse du dresseur (vitesse du background aussi)
        self.sacha = sacha # Représente le pokedex du joueur 

        

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def distance(self, pokemon):
        # Renvoie la distance du dresseur à un pokemon
        return np.sqrt((self.x - pokemon.x)**2 + (self.y - pokemon.y)**2)

    def proche(self, pokemons_sauvages):
        """
            Renvoie un couple :
            True si assez proche d'un pokemon sauvage, et l'indice dans la liste pokemons_sauvage correspondant au pokemon recontré
        """

        for nom_pokemon, pokemon in pokemons_sauvages.pokedex.items():
            if self.distance(pokemon) <= self.DISTANCE_COMBAT:
                return (True, pokemon)
            
        return (False, pokemon)
    
    def proche_affichage(self, pokemon):
        if self.distance(pokemon) <= self.DISTANCE_AFFICHAGE:
            return True
        
    

