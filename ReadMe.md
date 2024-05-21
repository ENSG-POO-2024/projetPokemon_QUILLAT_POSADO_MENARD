# Pokémon: projet informatique de Diego, Rémi, Maël

Pour lancer le jeu, vous devez lancer Jeu.py

## Données disponibles

### Dans le répertoire "Media", vous avez:

* un dossier contenant les images d'affichage du dresseur Pokémon
* un dossier Types contenant les images des différents types des Pokémons
* un dossier Image contenant différentes images nécessaires au bon affichage du jeu

### Dans le répertoire "Pokemons", vous avez:

* Un dossier pour chaque Pokémon 

* Chaque dossier possède un png de face ainsi que de dos et un gif de face et de dos pour chaque Pokémon

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

### Dans le répertoire "Starter", vous avez:

* Un fichier Starter.py qui sert à choisir son pokémon de départ, ce fichier sera appelé au moment voulu

* Des images nécessaires à l'affichage du fichier Starter.py


### D'autres fichiers python sont présents:

* Seul le fichier Jeu.py permet de jouer au jeu complet

* Chaque fichier possède un main qui permet de comprendre ce qu'affiche ou produit ce fichier mais ne permet pas de jouer correctement au jeu


### Map et Combat

* Les Pokémons apparaissent de manière aléatoire sur la Map et possèdent un taux de rareté ce qui fait qu’un Rattata peut apparaître plusieurs fois alors qu’un Artikodin a peu de chance d’apparaître. Les pokémons présents sur la map sont contenus dans le fichier pokemons_a_capturer.csv qui se ré écrit à chaque fois qu'une partie est lancée pour que les Pokémons ne soient pas toujours les mêmes

* Pour les combats vous avez plusieurs possibilités: utiliser l’attaque normale du Pokémon, utiliser son attaque spéciale ou changer de Pokémon. L’attaque normale du Pokémon repose sur ses statistiques d’attaque normale et les dégâts sont calculés de la manière suivante: partie entière de ((500 * attaque normale * coef de type / défense normale) diviser par 50) le tout + 2 (formule disponible dans la fonction attaquer du fichier Poke.py). Avec attaque normale la statistique d'attaque normale de l’attaquant et défense normale la statistique de défense normale du défenseur. Coef de type correspond au multiplicateur de type, en effet les Pokémons possèdent des types et certains sont forts contre d’autres et faibles contre certains. Le détail des coefficients est donné dans le rapport d'analyse. Pour l’attaque spéciale elle utilise la même formule mais avec les statistiques spéciales des Pokémons, cette attaque spéciale n’est disponible que tous les 2 tours et n’est pas forcément plus efficace car certains Pokémons ont des statistiques d'attaque spéciales plus faibles que l’attaque normale. Au dresseur de bien choisir et de bien connaître ses Pokémons. Pour changer de Pokémon il faut en posséder au moins 2 et le fait de changer vous utilisera un tour. Notre mode de combat fonctionne au tour par tour, on commence par attaquer ou changer de Pokémon ensuite le Pokémon sauvage contre-attaque. Le combat se finit quand le Pokémon adverse n’a plus de HP (point de vie) ou que tous vos Pokémons n’ont plus de HP. Une fois le combat fini vous pouvez choisir entre capturer le Pokémon ou partir sans le capturer.


### Pour jouer pleinement au jeu:

* Il est nécessaire d'installer PyQt5, vous pouvez écrire "pip install PyQt5" dans votre terminal si vous possédez pip

* Il est nécessaire d'installer pygame, vous pouvez écrire "pip install pygame" dans votre terminal si vous possédez pip
(pygame n'est utilisé que pour emettre un son au moment du combat)

* Il est nécessaire d'installer cv2, vous pouvez écrire "pip install cv2" dans votre terminal si vous possédez pip (cela ne sert qu'à afficher la vidéo de présentation)

* Pour une meilleure expérience visuelle vous pouvez télécharger les polices d'écriture "Minecraft" et "Hello World":
    - https://www.dafont.com/fr/minecraft.font
    - https://www.dafont.com/hello-world.font





