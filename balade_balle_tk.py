
### Déplacement d'une balle à l'aide
### d'un bouton d'un bord à 
### l'autre et d'un 2ème bouton pour un ### déplacement circulaire dans un canva. '

from tkinter import *
import math

# Marche
def sens_h(event=None):
    marche("horizon")

def sens_c(event=None):
    marche("circus")
    
def marche(sens):
    global en_marche,sens_h
    en_marche = True
    if sens == "horizon":
        avance_rond_droit()
    if sens == "circus":
        avance_rond_circulaire()

# Arrêt
def arret(event=None):
    global en_marche
    en_marche = False

# déplacement horizontal de bord à bord du canevas
def avance_rond_droit():
    global x1, y1, x, en_marche
    if en_marche:
        if x1 == 20:
            x = 5
        if x1 == 385:
            x = - 5
        x1, y1 = x1+x, y1
        can.coords(rond,x1-15,y1-15,x1+15,y1+15)
        can.after(10,avance_rond_droit)
        
# déplacement circulaire
def avance_rond_circulaire():
    global angle, rond, can
    if en_marche:
        # Calcul des déplacements en x et y à partir de l'angle
        x1 = math.cos(math.radians(angle)) * vitesse
        y1= -math.sin(math.radians(angle)) * vitesse
    
        # Déplacement du cercle
        can.move(rond, x1, y1)
    
        # Actualisation de l'angle
        angle += 1
    
        # Appeler cette fonction à nouveau après un délai pour créer une animation
        can.after(10,avance_rond_circulaire)
        
# partie principales
##############
x1, y1 = 20, 200
x = 5 # variable pour changer le sens de déplacement de la balle

# Initialisation de l'angle et de la vitesse de déplacement
angle = 0
vitesse = 2

fen = Tk() # widget principal
fen.title('Balade balle')

### widgets esclaves ###

# Canva qui contient le rond qui se déplace
can = Canvas(fen,width=400,height=400,bg='white')
can.grid(column=1,row=1)

cadre = Frame(fen)
cadre.grid(column=1,row=2,pady=10)

#Rond rouge que l'on déplace à l'aide d'un bouton. Soit l'horizontal. Soit le circulaire.
rond = can.create_oval(x1-15,y1-15,x1+15,y1+15,width=2,fill='red')

# N°1 Bouton_horizon pour déplacer le rond
bouton_horizon = Button(cadre,text='<------>',command=arret,width=5,bg='white')
bouton_horizon.grid(column=1,row=1,padx=5)

# Bouton_horizon pressé
bouton_horizon.bind('<ButtonPress>',sens_h)

# Bouton_horizon relaché
bouton_horizon.bind('<ButtonRelease>', arret)

# N°2 Bouton_circulaire pour déplacer le rond en un mouvement circulaire.
bouton_circulaire = Button(cadre,text='O',command=arret,width=5,bg='white')
bouton_circulaire.grid(column=2,row=1,padx=5)

# aide
Label(fen,text=" maintien appuyé l'un des boutons ",bg="white").grid(column=1,row=3)

# Bouton_circulaire pressé
bouton_circulaire.bind('<ButtonPress>',sens_c)

# Bouton_circulaire relaché
bouton_circulaire.bind('<ButtonRelease>', arret)

# Variable de controle de fonctionnement
en_marche = False

# Bouton pour quitter l'application
Button(fen,text='Quitter',command=fen.destroy,bg='white').grid(column=1,row=4,pady=10)

fen.mainloop()