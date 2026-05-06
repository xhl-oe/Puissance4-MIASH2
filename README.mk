Le jeu Puissance 4 est un jeu réalisé par Khery, Jehane, Chloé et Amine, des étudiants de L1 MIASHS. 
C'est un jeu qui se joue à deux joueurs, chaque joueur a une couleur. Il y a une grille verticale qui possèdent 7 colonnes et 6 lignes.(a l'origine)

COMMENT CE JEU SE DEROULE-T-IL ? 
A tour de rôle, les joueurs mettent un jeton qu'ils auront choisi. Le jeton se pose soit en bas de la grille soit sur un jeton. 

LE BUT DU JEU 
Pour gagner, il faut aligner 4 jetons (a l'origine) soit :
 - horizontalement 
 - verticalement
 - en diagonale 

Voici le lien qui dirige vers notre projet : (https://github.com/xhl-oe/Puissance4-MIASH2/blob/main/interface.py)

DOCUMENTATION SUR LE PROGRAMME PYTHON : 
Nous avons tout d'abord fais les dimensions de l'interface et de la grille, la mise en place des noms des joueurs, du scrore de départ et aussi l'objectif à atteindre pour gagner.
Ensuite, nous avons fais une boucle afin de créer une grille vide. Nous nous sommes ensuite attaquer a l'affichage du menu de départ, où les joueurs peuvent mettre leur pseudos mais où ils peuvent aussi accéder aux paramètres de la grille ou encore du nombre de jetons à aligner pour gagner.
Puis, nous avons fais un menu afin que le ou les joueur(s) décident soit de jouer contre de l'IA ou une autre personne, soit de quitter le jeu ou encore avoir de l'aide.
Nous avons par la suite aborder l'esthétique de la grille avant d'ajouter les différentes manières de gagner. 
Nous avons mis des fonctions afin de réinitialisé la grille afin de faire une nouvelle partie ou une nouvelle manche. Grâce au langage Python, nous avons fais en sortent d'alterner le joueur qui débute la partie.
Noux avons créer un fonction afin que les joueurs puissent cliquer sur les cases afin de jouer.
Nous avons mis en place une vérification afin de savoir si un joueur a gagne ou si lz grille s'est remplie sans qu'il y est de vainqueur.
Nous avons créer un historique afin de permettre aux joueurs, s'ils le souhaitent, d'annuler leur coup tout en souvegardant la partie telle quelle.
La dernière fonction permet de lancer le jeu.
Nous avons fini notre programme ou rebasculant sur l'esthétique des boutons "jouer" et "recommencer", le basculement de la page d'acceuil à la page de jeu ainsi que l'affichage du score.
