#a l'aide du cours en ligne OrdiRoutier(sur YouTube)on cree une inetrface
import tkinter as tk

fenetre = tk.Tk()

fenetre.geometry("560x480")  # correction ici
fenetre.title("Puissance 4")
#fenetre.["zffedser"]="red"
#fenetre.resizable(height=False,width=False)

label=tk.Label(fenetre,text="Puissance 4♥",font=("verdana",24,"italic"),fg="PaleVioletRed",bg="pink")#PaleVioletRed=#DB7093
#label.pack(side=RIGHT,padx=10)
label.pack() 
sub_label=tk.Label(fenetre,text="by Khery,Jehane,Chloe,Amine",font=("verdana",12,"italic"),fg="PaleVioletRed",bg="pink")
sub_label.pack()
#sub_label["texte"]="nimporte quel texte"#pour changer le texte de sub_label comme pour une liste
#def jouer():
  
def bouton_jouer():
    print("le jeu commenceavec {nom1} et {nom2}")
bouton = tk.Button(fenetre, text="Jouer", font=("verdana", 30, "italic"), fg="PaleVioletRed", bg="pink", command=bouton_jouer,padx=70)
bouton.pack(pady=100)

def jouer():
    nom_joueur1 = entree1.get()
    nom_joueur2 = entree2.get()
    if not nom_joueur1 or not nom_joueur2:
        print("Veuillez entrer deux pseudos")
        return
    if nom_joueur1 == nom_joueur2:
        print("Pseudo déjà pris")
        return

    print(f"Le joueur {nom_joueur1} est rentré dans le jeu")
    print(f"Le joueur {nom_joueur2} est rentré dans le jeu")

nom_joueur1 = tk.StringVar()
nom_joueur2 = tk.StringVar()
label1=tk.Label(fenetre,text="Entrez pseudo joueur 1",font=("verdana",12,),fg="PaleVioletRed",bg="pink")
label1.pack()

entree1=tk.Entry(fenetre,textvariable= nom_joueur1,font=("verdana",12,),fg="PaleVioletRed",bg="pink")
entree1.pack()

label2=tk.Label(fenetre,text="Entrez pseudo joueur 2",font=("verdana",12,),fg="PaleVioletRed",bg="pink")
label2.pack()

entree2=tk.Entry(fenetre,textvariable=nom_joueur2,font=("verdana",12,),fg="PaleVioletRed",bg="pink")
entree2.pack()

bouton=tk.Button(fenetre,text="Valider",font=("verdana",12,),fg="PaleVioletRed",bg="pink",command=jouer)
bouton.pack()

mon_menu = tk.Menu(fenetre)

#les sous onglets
Jouer=tk.Menu(mon_menu,tearoff=0)
Jouer.add_command(label="jouer en 1v1")
Jouer.add_command(label="jouer contre l'ia")

Quitter=tk.Menu(mon_menu,tearoff=0)
Quitter.add_command(label="Quitter le jeux")

Aide=tk.Menu(mon_menu,tearoff=0)#tearoff=0 pour ne pas pouvoir detacher le menu
Aide.add_command(label="Règles du jeux")
Aide.add_command(label="Menu d'aide")
Aide.add_command(label="Modifier les paramètres du jeux")
#Les menues du jeux
mon_menu.add_cascade(label="Jouer                                                                    ",menu=Jouer)
mon_menu.add_cascade(label="Aide                                                                    ",menu=Aide)
mon_menu.add_cascade(label="Quitter",menu=Quitter)

fenetre.config(menu=mon_menu) #pour afficher le menu dans la fenetre







fenetre.mainloop() #boucle pour afficher la fenetre et la maintenir ouverte

