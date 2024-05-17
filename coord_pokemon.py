import os
import pandas as pd
import random


def generer_coordonnees_uniques(nombre_lignes):
    coordonnees_uniques = set()
    while len(coordonnees_uniques) < nombre_lignes:
        x = random.randint(4, 41) * 110
        y = random.randint(4, 41) * 110
        if 2310 <= x <= 2530 or 2200 <= y <= 2420:
           pass
        else:
            coordonnees_uniques.add((int(x), int(y)))
    return list(coordonnees_uniques)


def poke_coord(fichier_entree, fichier_sortie, nombre_lignes):
    # On prend le chemin du répertoire parent du script Python
    chemin_parent = os.path.dirname(os.path.abspath(__file__))
    # On construit le chemin complet du fichier CSV en joignant le chemin du répertoire parent avec le répertoire "data" et le nom du fichier
    chemin_fichier = os.path.join(chemin_parent, 'data', fichier_entree)
    # On charge le fichier CSV en tant que DataFrame avec Pandas
    df = pd.read_csv(chemin_fichier)

    # Calculer les poids de rareté en fonction des valeurs de rareté
    poids_rarete = df['Rare'].apply(lambda x: x)  

    # Sélectionner aléatoirement des lignes avec remplacement, en tenant compte des poids de rareté
    lignes_aleatoires = df.sample(n=nombre_lignes, replace=True, weights=poids_rarete)

    # Générer les coordonnées uniques pour X et Y
    coordonnees = generer_coordonnees_uniques(nombre_lignes)

    # Ajouter les colonnes X et Y au DataFrame
    lignes_aleatoires['X'] = [x for x, _ in coordonnees]
    lignes_aleatoires['Y'] = [y for _, y in coordonnees]

    # Écrire les lignes dans un nouveau fichier CSV
    # Enregistrer le DataFrame modifié dans le fichier CSV d'origine
    chemin_fichier = os.path.join('data', fichier_sortie)
    lignes_aleatoires.to_csv(chemin_fichier, index=False)


if __name__ == '__main__':
    pokemons_sauvages = poke_coord('pokemon_first_gen.csv', 'pokemons_a_capturer.csv', 10)


