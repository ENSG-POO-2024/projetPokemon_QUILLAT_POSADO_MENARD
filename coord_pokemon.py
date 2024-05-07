
import pandas as pd
import numpy as np
import os


def coord_poke():

    # Charger le fichier CSV dans un DataFrame
    # On prend le chemin du répertoire parent du script Python
    chemin_parent = os.path.dirname(os.path.abspath(__file__))
    # On construit le chemin complet du fichier CSV en joignant le chemin du répertoire parent avec le répertoire "data" et le nom du fichier
    chemin_fichier = os.path.join(chemin_parent, 'data', 'pokemons_a_capturer.csv')
    # On charge le fichier CSV en tant que DataFrame avec Pandas
    df = pd.read_csv(chemin_fichier)

    # Générer de nouvelles valeurs pour X et Y
    def generer_nouvelles_valeurs(df):
        # Générer des valeurs aléatoires multiples de 110
        def generer_valeur():
            return np.random.randint(4, 42) * 110

        # Générer de nouveaux couples (X, Y)
        nouveaux_couples = set()
        for _ in range(len(df)):
            x, y = generer_valeur(), generer_valeur()
            while (x, y) in nouveaux_couples:
                x, y = generer_valeur(), generer_valeur()
            nouveaux_couples.add((x, y))
            yield x, y

    # Écraser les valeurs existantes de X et Y par les nouvelles valeurs
    df['X'], df['Y'] = zip(*generer_nouvelles_valeurs(df))

    # Enregistrer le DataFrame modifié dans le fichier CSV d'origine
    chemin_fichier = os.path.join('data', 'pokemons_a_capturer.csv')
    df.to_csv(chemin_fichier, index=False)
