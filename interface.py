# chloe
import tkinter as tk
import random
fenetre = tk.Tk()
fenetre.geometry("560x520")#Largeur de la fenêtre = 560 pixels, Hauteur de la fenêtre = 520 pixels
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

#  affichage sur l'interface du jeu au debut 
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


#khery
#ECRIRE SOURCE 
def ouvrir_parametres():#POUR ALLEZ PLUS LOIN n2: ouvrir une nouvelle fenêtre pour modifier les paramètres du jeu
    fenetre_param = tk.Toplevel(fenetre)#Crée une nouvelle fenêtre secondaire (une pop-up) liée à la fenêtre principale
    fenetre_param.title("Paramètres")
    fenetre_param.geometry("300x300")#300 pixels sur 300 pixels.
    tk.Label(fenetre_param, text="Colonnes").pack()
    entree_colonnes = tk.Entry(fenetre_param)
    entree_colonnes.insert(0, str(colonnes))#Met la valeur actuelle de colonnes dans le champ dès le début.
    entree_colonnes.pack()
    tk.Label(fenetre_param, text="Lignes").pack()
    entree_lignes = tk.Entry(fenetre_param)
    entree_lignes.insert(0, str(lignes))
    entree_lignes.pack()
    tk.Label(fenetre_param, text="Jetons pour gagner").pack()
    entree_alignement = tk.Entry(fenetre_param)
    entree_alignement.insert(0, str(alignement_gagnant))
    entree_alignement.pack()

    def sauvegarder():#TOUJOURS POUR ALLEZ PLUS LOIN n2: sauvegarder les paramètres modifiés et mettre à jour la grille en conséquence
        global colonnes, lignes, alignement_gagnant
        global grille_logique
        #Récupère ce que l’utilisateur a écrit dans les champs et les convertit en nombres (int):
        colonnes = int(entree_colonnes.get())
        lignes = int(entree_lignes.get())
        alignement_gagnant = int(entree_alignement.get())

        # recréer grille logique
        grille_logique = []
        for i in range(lignes):
            ligne = []
            for j in range(colonnes):
                ligne.append(0)
            grille_logique.append(ligne)
        # changer taille canvas
        canvas.config(width=colonnes * taille_case,height=lignes * taille_case)
        creer_grille()
        fenetre_param.destroy()#Ferme la fenêtre de paramètres après avoir sauvegardé les modifications.
    bouton_valider = tk.Button(fenetre_param,text="Valider",command=sauvegarder)
    bouton_valider.pack(pady=10)

#CHLOE:
# MENU
mon_menu = tk.Menu(fenetre)

jouer = tk.Menu(mon_menu, tearoff=0)#tearoff=0 empêche le menu de se détacher de la fenêtre principale
jouer.add_command(label="jouer en 1v1",command=lambda: choisir_mode("1v1"))
jouer.add_command(label="jouer contre l'ia",command=lambda: choisir_mode("ia"))

Quitter = tk.Menu(mon_menu, tearoff=0)
Quitter.add_command(label="Quitter le jeu", command=fenetre.quit)#Permet de fermer la fenêtre et de quitter le programme lorsque l'utilisateur sélectionne cette option dans le menu.

Aide = tk.Menu(mon_menu, tearoff=0)
Aide.add_command(label="Règles du jeu")
Aide.add_command(label="Menu d'aide")
Aide.add_command(label="Modifier les paramètres du jeu",command=ouvrir_parametres)#Permet d'ouvrir la fenêtre de paramètres lorsque l'utilisateur sélectionne cette option dans le menu d'aide.

mon_menu.add_cascade(label="Jouer", menu=jouer)
mon_menu.add_cascade(label="Aide", menu=Aide)
mon_menu.add_cascade(label="Quitter", menu=Quitter)

fenetre.config(menu=mon_menu)

# creer bouton annuler le coup d'avant
bouton_annuler = tk.Button(fenetre,text="Annuler coup",font=("verdana", 12),fg="white",bg="gray")

#JEHANE
# Grille graphique
grille_graphique = []

canvas = tk.Canvas(fenetre,width=420, height=360, bg="white")#Largeur420 pixels.Hauteur du canvas = 360 pixels
# CREATION DE LA GRILLE
def creer_grille():
    """Crée et affiche la grille graphique du jeu sur le canvas."""
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


#CHLOE:
def grille_pleine():
    """Vérifie si la grille est complètement remplie."""

    for ligne in grille_logique:
        if 0 in ligne:
            return False

    return True

#AMINE:
# VERIFICATION VICTOIRE
def verifier_victoire(joueur):
    """Vérifie si le joueur a gagné."""

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
#AMINE:
# RESET
def reset():
    """Réinitialise la partie tout en conservant les scores des joueurs."""
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

#AMINE:
#POUR ALLEZ PLUS LOIN n1:
def reset_partie():
    """Réinitialise la partie entière, y compris les scores, pour recommencer une nouvelle partie à zéro."""
    global score1, score2
    score1 = 0
    score2 = 0
    score_label.config(text=nom1 + " : 0 | " + nom2 + " : 0")
    reset()

#AMINE:
def nouvelle_manche():
    """Alterne le joueur qui commence la nouvelle manche et réinitialise la grille pour une nouvelle partie, tout en conservant les scores."""
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

# Historique des coups
historique = []
#JEHANE:
# CLIQUE SUR LE PLATEAU
def cliquer(event):
    """Gère le clic de l'utilisateur sur le plateau de jeu."""
    global joueur_actuel
    col = event.x // taille_case # Convertit la position x du clic en numéro de colonne (0 à 6)(cours en ligne d'Ordi Routier)
    if col < 0 or col >= colonnes:
        return# Si le clic est en dehors de la grille, on ignore le clic

    for ligne in range(lignes - 1, -1, -1):#on simule la gravité en partant du bas de la colonne vers le haut pour trouver la première case vide
        if grille_logique[ligne][col] == 0:
            grille_logique[ligne][col] = joueur_actuel

            historique.append((ligne, col))

            couleur = "lightblue" if joueur_actuel == 1 else "lightgreen"

            canvas.itemconfig(grille_graphique[ligne][col],fill=couleur)

            # Vérifie victoire
            if verifier_victoire(joueur_actuel):
                #POUR ALLEZ PLUS LOIN n1:
                global score1, score2
                gagnant = nom1 if joueur_actuel == 1 else nom2
                if joueur_actuel == 1:
                    score1 += 1

                else:
                    score2 += 1
                score_label.config(text=nom1 + " : " + str(score1) +" | " +nom2 + " : " + str(score2))
                
                #victoire finale
                if score1 == manches_pour_gagner:
                    message.config(text=nom1 + " remporte la partie !")
                    fenetre.after(3000, reset_partie)#attendre 3000 millisecondes avant d'appeler la fonction reset_partie
                    canvas.unbind("<Button-1>")
                    return

                if score2 == manches_pour_gagner:
                    message.config(text=nom2 + " remporte la partie !")
                    fenetre.after(3000, reset_partie)#attendre 3000 millisecondesavant d'appeler la fonction reset_partie
                    canvas.unbind("<Button-1>")#ete désactive le clic sur le canvas pour éviter que les joueurs continuent à jouer après la fin de la partie
                    return
                message.config(text=gagnant + " gagne la manche !")
                fenetre.after(3000, nouvelle_manche)
                canvas.unbind("<Button-1>")
                return
            
            if grille_pleine():
                message.config(text="Match nul !")
                canvas.unbind("<Button-1>")
                return

#CHLOE:
            # Changer joueur
            joueur_actuel = 2 if joueur_actuel == 1 else 1

            # tour de l'IA
            if mode_jeu == "ia" and joueur_actuel == 2:

                fenetre.after(500, jouer_ia)

            return
            
# ANNULER COUP
def annuler_coup():

    global joueur_actuel

    if not historique:
        message.config(text="Aucun coup à annuler")
        return

    ligne, col = historique.pop()

    grille_logique[ligne][col] = 0

    canvas.itemconfig(grille_graphique[ligne][col],fill="lightpink")

    joueur_actuel = 2 if joueur_actuel == 1 else 1

    message.config(text=nom1 + " vs " + nom2)

    canvas.bind("<Button-1>", cliquer)


bouton_annuler.config(command=annuler_coup)
#JEHANE:
#POUR ALLEZ PLUS LOIN n3
def choisir_mode(mode):
    """Choisit le mode de jeu et met à jour l'interface en conséquence."""
    global mode_jeu
    mode_jeu = mode
    if mode == "ia":
        entree2.config(state="normal")
        entree2.delete(0, tk.END)
        entree2.insert(0, "IA")
        entree2.config(state="disabled")
    else:
        entree2.config(state="normal")
        entree2.delete(0, tk.END)

#KHERY:
#POUR ALLEZ PLUS LOIN n3:
def jouer_ia():
    colonnes_valides=[]
    # Vérifie les colonnes qui ne sont pas pleines
    for col in range(colonnes):
        if grille_logique[0][col] == 0:
            colonnes_valides.append(col)
    # Si aucune colonne n'est valide, on ne fait rien
    if not colonnes_valides:
        return
    # Choisit une colonne aléatoire parmi les colonnes valides
    col_ia = random.choice(colonnes_valides)
    #place le jeton de l'ia dans la colonne choisie
    for ligne in range(lignes - 1, -1, -1):
        if grille_logique[ligne][col_ia] == 0:
            grille_logique[ligne][col_ia] = 2
            historique.append((ligne, col_ia))
            canvas.itemconfig(grille_graphique[ligne][col_ia],fill="lightgreen")
            
        #victoire ia 
            global score2
            if verifier_victoire(2):
                score2 += 1
                score_label.config(
                    text=nom1 + " : " + str(score1)+ " | " + nom2 + " : " + str(score2))
                message.config(text="L'IA gagne la manche !")
                fenetre.after(3000, nouvelle_manche)
                return

            # match nul
            if grille_pleine():
                message.config(text="Match nul !")
                return

            # rendre la main au joueur
            global joueur_actuel
            joueur_actuel = 1

            return


#CHLOE:
# LANCER LE JEU
def lancer_jeu():
    '''Démarre le jeu en récupérant les pseudos des joueurs, en initialisant la grille et en choisissant aléatoirement le joueur qui commence.'''
    global nom1, nom2, joueur_actuel
    global score1, score2, joueur_depart#POUR ALLEZ PLUS LOIN n1:
    nom1 = entree1.get()
    nom2 = entree2.get()
    #POUR ALLEZ PLUS LOIN n3: choisir le mode de jeu en fonction du bouton cliqué
    if mode_jeu == "ia":
        nom2 = "IA"

    if nom1 == "" or nom2 == "":
        message.config(text="Veuillez entrer deux pseudos")
        return
    if nom1 == nom2 and mode_jeu == "1v1":
        message.config(text="Pseudo déjà pris")
        return
    
    # Cache menu de départ
    label.pack_forget()
    sub_label.pack_forget()
    label1.pack_forget()
    entree1.pack_forget()
    label2.pack_forget()
    entree2.pack_forget()
    bouton.pack_forget()
    
#khery
bouton_annuler.pack()

    canvas.pack()

    creer_grille()
    
    joueur_actuel = random.randint(1,2) # Choisit aléatoirement le joueur qui commence

    historique.clear()
    #POUR ALLEZ PLUS LOIN n1:
    score1 = 0
    score2 = 0
    score_label.config(text=nom1 + " : 0 | " + nom2 + " : 0")
    joueur_depart = random.randint(1,2)
    joueur_actuel = joueur_depart
    premier = nom1 if joueur_actuel == 1 else nom2

    message.config(text=premier + " commence !")
    canvas.bind("<Button-1>", cliquer)
    if mode_jeu == "ia" and joueur_actuel == 2:
        fenetre.after(500, jouer_ia)

# BOUTON JOUER
bouton = tk.Button(fenetre,text="Jouer",font=("verdana", 20, "italic"),fg="white",bg="PaleVioletRed",command=lancer_jeu)
bouton.pack(pady=20)

# BOUTON RESET
bouton_reset = tk.Button(fenetre,text="Recommencer",font=("verdana", 12),fg="PaleVioletRed", bg="white",command=reset)
bouton_reset.pack()

fenetre.mainloop()
    
    
