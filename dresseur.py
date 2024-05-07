#from mael import Pokemon
import numpy as np


class Dresseur:

    SIZE = 10
    DISTANCE_COMBAT = 3
    VITESSE_DEPART = 110
    
    def __init__(self, x, y, X, Y, lst_pokemons):
        self.x = x # x d'affichage
        self.y = y # x d'affichage
        self.X = X # X de coordonnées
        self.Y = Y # Y de coordonnées
        self.speed = self.VITESSE_DEPART
        self.pokedex = lst_pokemons

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
        cpt_pk = 0
        for pk in pokemons_sauvages:
            if self.distance(pk) <= self.DISTANCE_COMBAT:
                return (True, cpt_pk)
            cpt_pk += 1
        return (False, cpt_pk)
    
    def get_new_pokemon(self, pokemon):
        """
            Ajoute un pokemon au pokédex
        """
        copie_pokemon = pokemon.duplic() # méthode à écrire de copie de pokémon (pour qu'ils ne soient pas à la même adresse)
        self.pokedex.append(copie_pokemon)
    
    

    
if __name__ == "__main__":
    pk1 = Pokemon(2, 2)
    pk2 = Pokemon(5, 5)
    lst_pk = [pk2, pk1]
    d = Dresseur(1, 1, [])
    
    pk_proche = d.proche(lst_pk)
    if pk_proche[0]:
        id_pk = pk_proche[1]
        print(id_pk)