# dessine des trais de differentes couleurs

from tkinter import *
from random import randrange

# --- définition des fonctions gestionnaires d'événements : ---
def drawline():
  "Tracé d'une ligne dans le canevas can1"
  global x1, y1, x2, y2, coul
  can1.create_polygon(x1,y1,z1,x2,y2,z2,width=2,fill=coul)
# modification des coordonnées pour la ligne suivante :
  y2, y1 = y2+10, y1-10
  
def drawline2():
   global x5, y5 ,x6 ,y6, coul2
   can1.create_line(x5,y5,x6,y6,width=2,fill=coul2)
   global x3, y3, x4, y4
   can1.create_line(x3,y3,x4,y4,width=2,fill=coul2)
      
  
def changecolor():
  "Changement aléatoire de la couleur du tracé"
  global coul
  pal=['cyan','maroon','green']
  c = randrange(3) # => génère un nombre aléatoire de 0 à 3
  coul = pal[c]
  
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1, z1, x2, y2, z2 = 50, 200, 100, 300, 100, 100 # coordonnées de la ligne
x3, y3, x4,y4 = 0, 250, 600, 250 # coord de la croix
x5, y5, x6, y6 = 300, 0, 300, 600

coul = 'dark green' # couleur de la ligne
coul2 = 'red'

# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=500,width=600)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Viseur',command=drawline2)
bou3.pack()
bou4 = Button(fen1,text='Autre couleur',command=changecolor)
bou4.pack()
fen1.mainloop()  # démarrage du réceptionnaire d'événements
fen1.destroy() # destruction (fermeture) de la fenêtre