#JEHANE
# Création de la grille 6 lignes x 7 colonnes
lignes = 6
colonnes = 7
grille = []

for i in range(lignes):
    ligne = []
    for j in range(colonnes):
        ligne.append(" ")
    grille.append(ligne)

# Fonction pour afficher la grille
def afficher_grille():
    for ligne in grille:
        print("|", end=" ")
        for case in ligne:
            print(case, end=" | ")
        print()
    print("-" * (colonnes * 4))

#CHLOE
# Demander les noms des joueurs
nom_joueur1 = input("Nom du joueur 1 (Rouge) : ")
nom_joueur2 = input("Nom du joueur 2 (Jaune) : ")
# Joueurs : symbole + nom
joueurs = [("R", nom_joueur1), ("J", nom_joueur2)]
tour = 0
# Ajouter un jeton dans une colonne
def ajouter_jeton(colonne, symbole):
    i = lignes - 1
    while i >= 0:
        if grille[i][colonne] == " ":
            grille[i][colonne] = symbole
            return True
        i -= 1
    return False





#AMINE
# Vérifier si un joueur a gagné
def verifier_victoire(symbole):

    # Horizontal
    for i in range(lignes):
        for j in range(colonnes - 3):
            if grille[i][j] == symbole and grille[i][j+1] == symbole and grille[i][j+2] == symbole and grille[i][j+3] == symbole:
                return True

    # Vertical
    for i in range(lignes - 3):
        for j in range(colonnes):
            if grille[i][j] == symbole and grille[i+1][j] == symbole and grille[i+2][j] == symbole and grille[i+3][j] == symbole:
                return True

    # Diagonale descendante
    for i in range(lignes - 3):
        for j in range(colonnes - 3):
            if grille[i][j] == symbole and grille[i+1][j+1] == symbole and grille[i+2][j+2] == symbole and grille[i+3][j+3] == symbole:
                return True

    # Diagonale montante
    for i in range(3, lignes):
        for j in range(colonnes - 3):
            if grille[i][j] == symbole and grille[i-1][j+1] == symbole and grille[i-2][j+2] == symbole and grille[i-3][j+3] == symbole:
                return True

    return False




#KHERY
# Boucle principale du jeu
while True:

    afficher_grille()

    symbole, nom = joueurs[tour % 2]

    choix = input(f"{nom} ({symbole}), choisis une colonne (1-{colonnes}) : ")

    if not choix.isdigit():
        print("Merci d’entrer un nombre !")
        continue

    colonne = int(choix) - 1

    if colonne < 0 or colonne >= colonnes:
        print("Colonne invalide !")
        continue

    if not ajouter_jeton(colonne, symbole):
        print("Colonne pleine ! Essaie une autre.")
        continue

    if verifier_victoire(symbole):
        afficher_grille()
        print(f"{nom} gagne la partie !")
        break

    tour += 1