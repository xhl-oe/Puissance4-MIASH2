#JEHANE
# Grille graphique
grille_graphique = []

canvas = tk.Canvas(fenetre,width=420, height=360, bg="white")#Largeur420 pixels.Hauteur du canvas = 360 pixels
# CREATION DE LA GRILLE
def creer_grille():
    global grille_graphique
    grille_graphique = []
    canvas.delete("all")
    for ligne in range(lignes):
        ligne_tab = []
        for col in range(colonnes):
            x1 = col * taille_case# x1=0 pour la première colonne, x1=60 pour la deuxième colonne, etc.
            y1 = ligne * taille_case# y1=0 pour la première ligne, y1=60 pour la deuxième ligne, etc.
            x2 = x1 + taille_case # x2=60 pour la première colonne, x2=120 pour la deuxième colonne, etc.
            y2 = y1 + taille_case # y2=60 pour la première ligne, y2=120 pour la deuxième ligne, etc.

            case = canvas.create_oval(x1,y1,x2,y2,fill="lightpink", outline="black")
            ligne_tab.append(case)
        grille_graphique.append(ligne_tab)

def grille_pleine():

    for ligne in grille_logique:
        if 0 in ligne:
            return False

    return True

# VERIFICATION VICTOIRE
def verifier_victoire(joueur):

    # Horizontal
    for l in range(lignes):
        for c in range(colonnes - alignement_gagnant + 1):
            if all(grille_logique[l][c+i] == joueur for i in range(alignement_gagnant)):
                return True

    # Vertical
    for l in range(lignes - alignement_gagnant + 1):
        for c in range(colonnes):
            if all(grille_logique[l+i][c] == joueur for i in range(alignement_gagnant)):
                return True
    # Diagonale descendante
    for l in range(lignes - alignement_gagnant + 1):
        for c in range(colonnes - alignement_gagnant + 1):
            if all(grille_logique[l+i][c+i] == joueur for i in range(alignement_gagnant)):
                return True

    # Diagonale montante
    for l in range(alignement_gagnant - 1, lignes):
        for c in range(colonnes - alignement_gagnant + 1):
            if all(grille_logique[l-i][c+i] == joueur for i in range(alignement_gagnant)):
                return True

    return False
