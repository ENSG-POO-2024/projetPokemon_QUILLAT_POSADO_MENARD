# Pokémon: projet informatique de Diego, Rémi, Maël

## Données disponibles

### Dans le répertoire "Media", vous avez:

* un dossier contenant les images d'affichage du dresseur Pokémon
* un dossier Types contenant les images des différents types des Pokémons
* un dossier Image contenant différentes images nécessaires au bon affichage du jeu

### Dans le répertoire "data", vous avez:

* Un fichier csv contenant les 151 pokemons de la première génération, ainsi que leurs attributs :
  1. `#` : indique le numéro du pokemon (peut être utilisé comme id)
  2. `name` : le nom (ici en anglais) du pokemon
  3. `Type 1` : le type du pokemon
  4. `Type 2` : le second type du pokemon (s'il en possède un deuxième)
  5. `Total` : le nombre total de points d'attributs (HP + Attack + Defense + Sp. Attack + Sp. Def + Speed)
  6. `HP` : le nombre de point de vie de départ
  7. `Attack` : le nombre de point d'attaque (coefficient pour les dégats infligés)
  8. `Defense` : le nombre de point de défense (coefficient pour les dégats reçus)
  9. `Sp. Atk` : le nombre de point d'attaque spéciale (coefficient pour les dégats infligés)
  10. `Sp. Def` : le nombre de point de défense contre une attaque spéciale (coefficient pour les dégats reçus)
  11. `Speed` : la vitesse du pokemon (détermine qui joue en premier)
  12. `Generation` : la génération du pokemon (ici la première)
  13. `Legendary` : rareté du pokemon, les légendaires sont normalement uniques

* Un fichier csv contenant une liste de pokemons avec des coordonnées géographiques.

## Comment créer votre dépôt github ?

1. Se créer un identifiant github
2. Demander à un enseignant de vous ajouter dans l'organisation **ENSG-POO-2024**
3. *Forker* (copier) le projet **projetPokemon** et choisissez un nom très personnalisé !
4. Pour voir comment établir une connexion ssh entre votre ordinateur et github, voir documents/sshConnexion.md