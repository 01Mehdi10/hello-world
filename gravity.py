from tkinter import *
# procédure générale de déplacement :
def avance_lune(gd, hb):
 global x1, y1
 x1, y1 = x1 +gd, y1 +hb
 can1.coords(oval1, x1-30,y1-30, x1+30,y1+30)
 
# gestionnaires d'événements :
def depl_gauche_lune():
 avance_lune(-10, 0)
 distance_terre_lune()
def depl_droite_lune():
 avance_lune(10, 0)
 distance_terre_lune()
def depl_haut_lune():
 avance_lune(0, -10)
 distance_terre_lune()
def depl_bas_lune():
 avance_lune(0, 10)
 distance_terre_lune()
 
def avance_terre(gd, hb):
 global x2, y2
 x2, y2 = x2 +gd, y2 +hb
 can1.coords(oval2, x2-80,y2-80, x2+80,y2+80)
 
def distance_terre_lune():
 global ech
 distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
 
 Fg = G * (p_terre * p_lune)/distance**2
 Fg = round(Fg,2) # force gravitationnelle

 if distance < (80/4 + 30/4):  # Si les astres se chevauchent
   e_astres.config(text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance : 0 km \n Force gravitationnelle : \n' + str(Fg))
 else:
   distance = round(distance * ech, 2)
   e_astres.config(text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance : ' + str(distance) + ' km \n Force gravitationnelle : \n' + str(Fg))
 
# gestionnaires d'événements :
def depl_gauche():
 avance_terre(-10, 0)
 distance_terre_lune()
def depl_droite():
 avance_terre(10, 0)
 distance_terre_lune()
def depl_haut():
 avance_terre(0, -10)
 distance_terre_lune()
def depl_bas():
 avance_terre(0, 10)
 distance_terre_lune()
    
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
    
ech = 600000/600 # calcul échelle de distance

x1, y1 = 200, 200  # coordonnées initiales de la lune
x2, y2 = 350,350 # coordonnées initiales de la terre

# Calcul distance de la terre à la lune
Dx = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5*ech,2)

# masses de la terre et de la lune        
p_terre, p_lune = 5.972 * 10 ** 24,  7.342 * 10 ** 22 

G = 6.674*10**-11 # constante de la gravitation

Fg = G * (p_terre * p_lune)/Dx**2
Fg = round(Fg,2) # force gravitationnelle

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "esclaves" :
m_astres = Label(fen1,text='Masse de la terre = ' + str(p_terre)+'\n Masse de la lune ='+str(p_lune))
m_astres.grid(column=1,columnspan=4,row=1)
can1 = Canvas(fen1,bg='dark grey',height=600,width=600)
oval1 = can1.create_oval(x1-30,y1-30,x1+30,y1+30,width=2,fill='yellow') # lune
oval2 = can1.create_oval(x2-80,y2-80,x2+80,y2+80,width=2,fill='blue') #terre
can1.grid(column=1,columnspan=4,row=2)
e_astres = Label(fen1,text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance : ' + str(Dx) + ' km \n Force gravitationnelle : \n' + str(Fg)) # échelle de distance, distance entre les astres, force gravitationnelle
e_astres.grid(column=1,columnspan=4,row=3)
# Boutons lune
Button(fen1,text='Haut',command=depl_haut_lune,width=3).grid(column=3,row=4)
Button(fen1,text='Gauche',command=depl_gauche_lune,width=3).grid(column=2,row=5)
Button(fen1,text='Droite',command=depl_droite_lune,width=3).grid(column=4,row=5)
Button(fen1,text='Bas',command=depl_bas_lune,width=3).grid(column=3,row=6)

sep = Label(fen1,text='\n')
sep.grid(column=1,columnspan=4,row=7)
# Boutons terre
Button(fen1,text='Haut',command=depl_haut,width=3).grid(column=3,row=8)
Button(fen1,text='Gauche',command=depl_gauche,width=3).grid(column=2,row=9)
Button(fen1,text='Droite',command=depl_droite,width=3).grid(column=4,row=9)
Button(fen1,text='Bas',command=depl_bas,width=3).grid(column=3,row=10)
Button(fen1,text='Quitter',command=fen1.quit).grid()
# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()
