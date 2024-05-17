
####### Bibliothèques #######
from math import *
import pandas as pd
import os
from abc import *

####### Code #######

class Pokemon:
    def __init__(self, name, x, y, hp, attack, defense, sp_attack, sp_defense, type_):
        self.name = name
        self.x = x
        self.y = y
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.type = type_ #pour eviter le type déjà existant en python on met type_ mais il devient l'attribut type dans la suite

    @classmethod
    def creer_pokemon(cls, name, x, y, hp, attack, defense, sp_attack, sp_defense, type_):
        return cls(name, x, y, hp, attack, defense, sp_attack, sp_defense, type_)


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
        degats = int(500*self.attack*self.modifier(adversaire.type)/adversaire.defense)//50 + 2
        if degats <= 0:
            degats = 0
        elif degats >= adversaire.hp:
            degats = adversaire.hp
        adversaire.hp -= degats

        if adversaire.hp < 0:
                adversaire.hp = 0

        print(f"{self.name} attaque {adversaire.name.split()[0]} et lui inflige {degats} dégâts.")
        print(f"Il reste {adversaire.hp} points de vie à {adversaire.name.split()[0]}.")

        return degats

    def attaque_speciale_joueur(self, adversaire):
        # Utilise l'attaque spéciale
        degats = int(500*self.sp_attack*self.modifier(adversaire.type)/adversaire.sp_defense)//50 + 2
        if degats <= 0:
            degats = 0
        elif degats >= adversaire.hp:
            degats = adversaire.hp
        adversaire.hp -= degats  
        
        if adversaire.hp < 0:
            adversaire.hp = 0

        print(f"{self.name} utilise son attaque spéciale sur {adversaire.name.split()[0]} et lui inflige {degats} dégâts.")
        print(f"Il reste {adversaire.hp} points de vie à {adversaire.name.split()[0]}.")

        return degats
        

        

class Type(Pokemon):
    def __init__(self, name, fort=[], faible=[], neutre=[]):
        super().__init__(name, None, None, None, None, None, None, None, None)
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
        noms_pokemon = {}
        for index, row in data.iterrows():
            name = row['Name']  
            if name not in noms_pokemon:
                noms_pokemon[name] = 1
            else:
                noms_pokemon[name] += 1
                name += ' ' + str(noms_pokemon[name])
            x = row['X']
            y = row['Y']
            hp = row['HP']
            attack = row['Attack']
            defense = row['Defense']
            sp_attack = row['Sp. Atk']
            sp_defense = row['Sp. Def']
            type_name = row['Type 1'] 
            type_obj = globals()[type_name]()
            pokemon = Pokemon(name, x, y, hp, attack, defense, sp_attack, sp_defense, type_obj)
            # On ajoute les Pokémons au dictionnaire avec leur nom comme clé
            self.pokedex[name] = pokemon

    def __str__(self):
        texte = ""
        for nom_pokemon, pokemon in self.pokedex.items():
            texte += "Nom: " + pokemon.name + "\n"
            texte += "X: " + str(pokemon.x) + "\n"
            texte += "Y: " + str(pokemon.y) + "\n"
            texte += "HP: " + str(pokemon.hp) + "\n"
            texte += "Attaque: " + str(pokemon.attack) + "\n"
            texte += "Défense: " + str(pokemon.defense) + "\n"
            texte += "Sp. Attaque: " + str(pokemon.sp_attack) + "\n"
            texte += "Sp. Défense: " + str(pokemon.sp_defense) + "\n"
            texte += "Type: " + pokemon.type.name + "\n" + "\n"
        return texte

class InventaireJoueur(Pokedex):
    def __init__(self):
        super().__init__()
        self.inventaire_joueur = {}

    def ajout_inventaire(self, pokemon): 
        if pokemon.name.split()[0] not in self.pokedex:
            # Si le nom du Pokémon n'existe pas dans l'inventaire du joueur, on l'ajoute directement
            pokemon.name = pokemon.name.split()[0]
            self.pokedex[pokemon.name] = pokemon
        else:
            pokemon.name = pokemon.name.split()[0]
            # Si le nom du Pokémon existe déjà, on trouve le prochain numéro de séquence disponible 
            # pour que deux pokémons n'aient pas le même nom
            sequence = 2
            new_name = f"{pokemon.name} {sequence}" # On travaille avec un dictionnaire donc on doit gérer les clés et en créé une nouvelle
            while new_name in self.pokedex:
                sequence += 1
                new_name = f"{pokemon.name} {sequence}"
            # On crée une copie du Pokémon avec le nom modifié pour éviter d'écraser la précédente clé
            pokemon_copie = Pokemon(new_name, pokemon.x, pokemon.y, pokemon.hp, pokemon.attack, pokemon.defense, pokemon.sp_attack, pokemon.sp_defense, pokemon.type)
            # On ajoute le Pokémon avec le nom modifié à l'inventaire du joueur
            self.pokedex[new_name] = pokemon_copie
        
        pokemon.x = None # Le pokemon est maintenant dans notre inventaire
        pokemon.y = None # il n'a plus de coordonnées

    def capturer_pokemon(self, adversaire, pokedex_sauvage, pokedex):
        pokedex_sauvage.pokedex.pop(adversaire.name)
        adversaire.hp = pokedex.pokedex[adversaire.name.split()[0]].hp
        adversaire.x = None
        adversaire.y = None
        self.ajout_inventaire(adversaire)



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
            equipe.ajout_inventaire(self.pokedex[pokemon_choisi]) 
            pokemons_disponibles.remove(pokemon_choisi)  # Retirer le pokémon choisi de la liste des pokémons disponibles

        self.afficher_pokedex()

        return equipe
    
    def toujours_vivant(self):
        for nom_poke, pokemon in self.pokedex.items():
            if pokemon.hp > 0:
                return True
        return False
    



if __name__ == '__main__':
    # Exemple d'utilisation
    pokedex = Pokedex()
    inventaire_joueur = InventaireJoueur()
    magicarpe = Pokemon.creer_pokemon("Magicarpe", 0, 0, 50, 20, 10, 35, 15, Eau())
    pokedex.charger_pokedex('pokemon_first_gen.csv')
    print(pokedex)
    inventaire_joueur.ajout_inventaire(magicarpe)
