# dessine des trais de differentes couleurs

from tkinter import *
from random import randrange

# --- définition des fonctions gestionnaires d'événements : ---
def drawbluecercle():
  "Tracé d'un cercle dans le canevas can1"
  global x1, y1, x2, y2
  can1.create_oval(x1,y1,x2, y2,width=4,outline='blue')
def drawredcercle():
  global x5, y5 ,x6 ,y6
  can1.create_oval(x5,y5,x6,y6,width=4,outline='red')
def drawblackcercle():
  global x3, y3, x4, y4
  can1.create_oval(x3,y3,x4,y4,width=4,outline='black')
def draworangecercle():
  global x7, y7, x8, y8
  can1.create_oval(x7,y7,x8,y8,width=4,outline='orange')
def drawgreencercle():
  global x9, y9, x10, y10
  can1.create_oval(x9,y9,x10,y10,width=4,outline='green')
      
  
def changecolor():
  "Changement aléatoire de la couleur du tracé"
  global coul
  pal=['cyan','maroon','green']
  c = randrange(3) # => génère un nombre aléatoire de 0 à 3
  coul = pal[c]
  
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1,  x2, y2 = 200, 100, 50, 250 # coordonnées du cercle
x3, y3, x4,y4 = 360, 100, 210, 250 # coord du cercle
x5, y5, x6, y6 = 520, 100, 370, 250
x7, y7, x8, y8 = 280, 200, 130, 350
x9, y9, x10, y10 = 440, 200, 290, 350


# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='white',height=500,width=600)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Anneau bleu',command=drawbluecercle)
bou2.pack()
bou3 = Button(fen1,text='Anneau noir',command=drawblackcercle)
bou3.pack()
bou4 = Button(fen1,text='Anneau rouge',command=drawredcercle)
bou4.pack()
bou5 = Button(fen1,text='Anneau jaune',command=draworangecercle)
bou5.pack()
bou6 = Button(fen1,text='Anneau vert',command=drawgreencercle)
bou6.pack()
fen1.mainloop()  # démarrage du réceptionnaire d'événements
fen1.destroy() # destruction (fermeture) de la fenêtre