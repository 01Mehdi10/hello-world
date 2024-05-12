
### Déplacement d'une balle à l'aide
### d'un bouton d'un bord à l'autre
### dans un canva. 

from tkinter import *

# Marche
def marche(event=None):
    global en_marche, x
    en_marche = True
    avance_rond()

# Arrêt
def arret(event=None):
    global en_marche
    en_marche = False

# Partie calcules
def avance_rond():
    global x1, y1, x, en_marche
    if en_marche:
        if x1 == 20:
            x = 5
        if x1 == 385:
            x = - 5
        x1, y1 = x1+x,100
        can.coords(rond,x1-15,y1-15,x1+15,y1+15)
        can.after(50,avance_rond)
        
# partie principales
##############
x1, y1 = 20, 100
x = 5 # variable pour changer le sens de déplacement de la balle

fen = Tk() # widget principal
fen.title('Balade balle')

### widgets esclaves ###

# Canva qui contient le rond qui se déplace
can = Canvas(fen,width=400,height=400,bg='white')
can.grid(column=1,row=1)

#Rond rouge que l'on déplace à l'aide d'un bouton'
rond = can.create_oval(x1-15,y1-15,x1+15,y1+15,width=2,fill='red')

# Bouton pour déplacer le rond
bouton = Button(fen,text='>',command=arret,width=5,bg='white')
bouton.grid(column=1,row=2,pady=10)

# Bouton pressé
bouton.bind('<ButtonPress>', marche)

# Bouton relaché
bouton.bind('<ButtonRelease>', arret)

# Variable de controle de fonctionnement
en_marche = False

# Bouton pour quitter l'application
Button(fen,text='Quitter',command=fen.destroy,bg='white').grid(sticky=SW)

fen.mainloop()