import Poke as poke  # Importer les classes nécessaires depuis Pokemon.py

class Combat:
    def __init__(self, equipe_joueur, pokemon_adverse):
        self.equipe_joueur = equipe_joueur
        self.pokemon_adverse = pokemon_adverse

    def commencer_combat(self):
        print("Le combat commence !")
        print(f"Pokémon adverse : {self.pokemon_adverse.name}")

        

# Exemple d'utilisation :
if __name__ == "__main__":
    # Création d'une équipe de joueur
    joueur = poke.InventaireJoueur()
    magicarpe = poke.Pokemon.creer_pokemon("Magicarpe", 50, 20, 10, 35, 15, poke.Eau(), False)
    joueur.inventory(magicarpe)
    joueur.creer_equipe()

    # Création d'un Pokémon adverse
    pokemon_adverse = poke.Pokemon("Pikachu", 100, 30, 20, 25, 25, poke.Eau(), False)

    # Création d'une instance de Combat
    combat = Combat(joueur, pokemon_adverse)
    combat.commencer_combat()