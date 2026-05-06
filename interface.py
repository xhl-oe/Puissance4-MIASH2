# chloe
import tkinter as tk
import random
fenetre = tk.Tk()
fenetre.geometry("560x520")
fenetre.title("Puissance 4")
fenetre.config(bg="pink")

# Variables globales
joueur_actuel = 1
nom1 = ""
nom2 = ""

# Dimensions de la grille
colonnes = 7
lignes = 6
taille_case = 60

#POUR ALLEZ PLUS LOIN n1:
score1 = 0
score2 = 0
manches_pour_gagner = 3
joueur_depart = 1

#POUR ALLEZ PLUS LOIN n2:
alignement_gagnant = 4

#POUR ALLEZ PLUS LOIN n3:
mode_jeu = "1v1"

# Grille logique
grille_logique = []
for i in range(lignes):
    ligne = []
    for j in range(colonnes):
        ligne.append(0)
    grille_logique.append(ligne)

#  affichage sur le menu de départ
label = tk.Label(fenetre,text="Puissance 4♥",font=("verdana", 24, "italic"),fg="PaleVioletRed",bg="pink")
label.pack()

sub_label = tk.Label(fenetre,text="by Khery,Jehane,Chloe,Amine",font=("verdana", 12, "italic"),fg="PaleVioletRed",bg="pink")
sub_label.pack()

# PSEUDOS
nom_joueur1 = tk.StringVar()
nom_joueur2 = tk.StringVar()

label1 = tk.Label(fenetre,text="Entrez pseudo joueur 1",font=("verdana", 12),fg="PaleVioletRed",bg="pink")
label1.pack()

entree1 = tk.Entry(fenetre, textvariable=nom_joueur1,font=("verdana", 12), fg="black",bg="white")
entree1.pack()

label2 = tk.Label(fenetre,text="Entrez pseudo joueur 2",font=("verdana", 12),fg="PaleVioletRed",bg="pink")
label2.pack()

entree2 = tk.Entry(fenetre,textvariable=nom_joueur2,font=("verdana", 12),fg="black",bg="white")
entree2.pack()

message = tk.Label(fenetre,text="",font=("verdana", 12),bg="pink",fg="red")
message.pack()

#POUR ALLEZ PLUS LOIN n1:
score_label = tk.Label(fenetre,text="",font=("verdana", 12),bg="pink",fg="blue")
score_label.pack()




#AMINE
# Grille graphique
grille_graphique = []
# MENU
mon_menu = tk.Menu(fenetre)

jouer = tk.Menu(mon_menu, tearoff=0)
jouer.add_command(label="jouer en 1v1",command=lambda: choisir_mode("1v1"))
jouer.add_command(label="jouer contre l'ia",command=lambda: choisir_mode("ia"))

Quitter = tk.Menu(mon_menu, tearoff=0)
Quitter.add_command(label="Quitter le jeu", command=fenetre.quit)

Aide = tk.Menu(mon_menu, tearoff=0)
Aide.add_command(label="Règles du jeu")
Aide.add_command(label="Menu d'aide")
Aide.add_command(label="Modifier les paramètres du jeu",command=ouvrir_parametres)

mon_menu.add_cascade(label="Jouer", menu=jouer)
mon_menu.add_cascade(label="Aide", menu=Aide)
mon_menu.add_cascade(label="Quitter", menu=Quitter)

fenetre.config(menu=mon_menu)

# creer bouton annuler le coup d'avant
bouton_annuler = tk.Button(fenetre,text="Annuler coup",font=("verdana", 12),fg="white",bg="gray")
canvas = tk.Canvas(fenetre,width=420, height=360, bg="white")#Largeur420 pixels.Hauteur du canvas = 360 pixels
#JEHANE

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


    #AMINE
# RESET
def reset():#Réinitialise la grille de jeu et les variables associées pour recommencer une nouvelle partie, tout en conservant les scores.
    global grille_logique, joueur_actuel
    grille_logique = []
    for i in range(lignes):
        ligne = []
        for j in range(colonnes):
            ligne.append(0)
        grille_logique.append(ligne)
    historique.clear()
    joueur_actuel = 1
    message.config(text=nom1 + " vs " + nom2)
    creer_grille()
    canvas.bind("<Button-1>", cliquer)

#POUR ALLEZ PLUS LOIN n1:
def reset_partie():#Réinitialise la partie entière, y compris les scores, pour recommencer une nouvelle partie à zéro.
    global score1, score2
    score1 = 0
    score2 = 0
    score_label.config(text=nom1 + " : 0 | " + nom2 + " : 0")
    reset()

#AMINE
def nouvelle_manche():#Alterne le joueur qui commence la nouvelle manche et réinitialise la grille pour une nouvelle partie, tout en conservant les scores.
    global grille_logique, joueur_actuel, joueur_depart
    # vide grille logique
    grille_logique = []
    for i in range(lignes):
        ligne = []
        for j in range(colonnes):
            ligne.append(0)
        grille_logique.append(ligne)
    historique.clear()
    creer_grille()
    # alterne le joueur qui commence
    joueur_depart = 2 if joueur_depart == 1 else 1
    joueur_actuel = joueur_depart
    premier = nom1 if joueur_actuel == 1 else nom2
    message.config(text="Nouvelle manche : " + premier + " commence")
    canvas.bind("<Button-1>", cliquer)


    
    return False
    # RESET
def reset():#Réinitialise la grille de jeu et les variables associées pour recommencer une nouvelle partie, tout en conservant les scores.
    global grille_logique, joueur_actuel
    grille_logique = []
    for i in range(lignes):
        ligne = []
        for j in range(colonnes):
            ligne.append(0)
        grille_logique.append(ligne)
    historique.clear()
    joueur_actuel = 1
    message.config(text=nom1 + " vs " + nom2)
    creer_grille()
    canvas.bind("<Button-1>", cliquer)

#POUR ALLEZ PLUS LOIN n1:
def reset_partie():#Réinitialise la partie entière, y compris les scores, pour recommencer une nouvelle partie à zéro.
    global score1, score2
    score1 = 0
    score2 = 0
    score_label.config(text=nom1 + " : 0 | " + nom2 + " : 0")
    reset()


def nouvelle_manche():#Alterne le joueur qui commence la nouvelle manche et réinitialise la grille pour une nouvelle partie, tout en conservant les scores.
    global grille_logique, joueur_actuel, joueur_depart
    # vide grille logique
    grille_logique = []
    for i in range(lignes):
        ligne = []
        for j in range(colonnes):
            ligne.append(0)
        grille_logique.append(ligne)
    historique.clear()
    creer_grille()
    # alterne le joueur qui commence
    joueur_depart = 2 if joueur_depart == 1 else 1
    joueur_actuel = joueur_depart
    premier = nom1 if joueur_actuel == 1 else nom2
    message.config(text="Nouvelle manche : " + premier + " commence")
    canvas.bind("<Button-1>", cliquer)
    
