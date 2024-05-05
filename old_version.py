#on doit faire une class??

# def charger_pokedex(fichier): ##on peut mettre dans Pokemon ?? --> appeler Pokemon dans Pokemon
#     pokedex = {}
#     # On prend le chemin du répertoire parent du script Python
#     chemin_parent = os.path.dirname(os.path.abspath(__file__))
#     # On construit le chemin complet du fichier CSV en joignant le chemin du répertoire parent avec le répertoire "data" et le nom du fichier
#     chemin_fichier = os.path.join(chemin_parent, 'data', fichier)
#     # On charge le fichier CSV en tant que DataFrame avec Pandas
#     data = pd.read_csv(chemin_fichier)
#     for index, row in data.iterrows():
#         name = row['Name']  
#         hp = row['HP']
#         attack = row['Attack']
#         defense = row['Defense']
#         sp_attack = row['Sp. Atk']
#         sp_defense = row['Sp. Def']
#         type_name = row['Type 1'] 
#         type_obj = globals()[type_name]()
#         pokemon = Pokemon(name, hp, attack, defense, sp_attack, sp_defense, type_obj)
#         # On ajoute les Pokémons au dictionnaire avec leur nom comme clé
#         pokedex[name] = pokemon
#     return pokedex

# def inventory(pokemon, inventaire_joueur): # inventaire_joueur doit être un dictionnaire
#     if pokemon.name not in inventaire_joueur:
#         # Si le nom du Pokémon n'existe pas dans l'inventaire du joueur, on l'ajoute directement
#         inventaire_joueur[pokemon.name] = pokemon
#     else:
#         # Si le nom du Pokémon existe déjà, on trouve le prochain numéro de séquence disponible 
#         # pour que deux pokémons n'aient pas le même nom
#         sequence = 2
#         new_name = f"{pokemon.name} {sequence}" # On travaille avec un dictionnaire donc on doit gérer les clés et en créé une nouvelle
#         while new_name in inventaire_joueur:
#             sequence += 1
#             new_name = f"{pokemon.name} {sequence}"
#         # On crée une copie du Pokémon avec le nom modifié pour éviter d'écraser la précédente clé
#         pokemon_copie = Pokemon(new_name, pokemon.hp, pokemon.attack, pokemon.defense, pokemon.sp_attack, pokemon.sp_defense, pokemon.type)
#         # On ajoute le Pokémon avec le nom modifié à l'inventaire du joueur
#         inventaire_joueur[new_name] = pokemon_copie



# def afficher_dico(pokedex): # utile que pour afficher des dictionnaires contenant des pokémons
#     for nom_pokemon, pokemon in pokedex.items():
#         print(f"Nom: {pokemon.name}")
#         print(f"HP: {pokemon.hp}")
#         print(f"Attaque: {pokemon.attack}")
#         print(f"Défense: {pokemon.defense}")
#         print(f"Sp. Attaque: {pokemon.sp_attack}")
#         print(f"Sp. Défense: {pokemon.sp_defense}")
#         print(f"Type: {pokemon.type.name}")
#         print()  # Ajouter une ligne vide entre chaque Pokémon


# def create_team(inventaire): # Inventaire doit être un dictionnaire
#     team = {}
#     for i in range(3): # Une équipe est composée de 3 pokémons
#         pokemon = input("Quel pokémon voulez-vous choisir pour rejoindre l'équipe ? ")
#         while pokemon not in inventaire or len(inventaire) <= 3-i :
#             print(f"'{nom_pokemon_test}' n'est pas présent dans vos pokémons.")
#         team[pokemon.name] = pokemon

#     return team