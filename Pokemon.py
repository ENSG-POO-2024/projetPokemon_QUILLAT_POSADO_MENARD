###Partie Maël

from math import *
import numpy as np
from abc import *

class Pokemon:
    def __init__(self, name, hp, attack, defense, type_):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.type = type_ #pour eviter le type de python on met type_

    @classmethod
    def creer_pokemon(cls, name, hp, attack, defense, type_):
        return cls(name, hp, attack, defense, type_)

    def attaquer(self, other_pokemon):
        print(f"{other_pokemon.name} a {other_pokemon.hp} hp et {other_pokemon.defense} point de defense et {self.name} a {self.attack} point d'attaque.")
        new_att = self.new_attack(other_pokemon.type)
        degats = new_att - other_pokemon.defense 
        other_pokemon.hp -= degats
        print(f"{self.name} attaque {other_pokemon.name} et lui inflige {degats} dégâts.")
        print(f"Il reste {other_pokemon.hp} point de vie à {other_pokemon.name}")

    def new_attack(self, type_adversaire):
        if type_adversaire.name in self.type.fort:
            return self.attack * 2
        elif type_adversaire.name in self.type.faible:
            return self.attack * 0.5
        elif type_adversaire.name in self.type.neutre:
            return 0
        else:
            return self.attack

        

class Type(Pokemon):
    def __init__(self, name, fort=[], faible=[], neutre=[]):
        super().__init__(name, None, None, None, None)
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
        super().__init__("Insecte", fort=["Plante", "Psy", "Tenenbres"], faible=["Acier", "Combat", "Feu", "Fee", "Poison", "Spectre", "Vol"], neutre=[])


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



# Création des Pokémon avec leurs types respectifs et des statistiques personnalisées
magicarpe = Pokemon.creer_pokemon("Magicarpe", 50, 20, 10, Eau())
charmander = Pokemon.creer_pokemon("Charmander", 70, 25, 15, Feu())
pikachu = Pokemon.creer_pokemon("Pikachu", 60, 30, 12, Electrik())

# Combat entre Pikachu et Magicarpe
pikachu.attaquer(magicarpe)

