#Création de la grille 6 lignes * 7 colonnes 
lignes = 6 
colonnes = 7 
grille = []

for i in range(lignes) : 
  ligne = []
  for j in range(colonnes) : 
    ligne.append(" ") 
  grille.append(ligne) 

#fonction pour afficher la grille 
def afficher_grille() : 
  for ligne in grille : 
    print("|", end=" ")
    for case in ligne : 
      print(case, end= " | ")
    print()
  print("-" * (colonnes * 4)) 
