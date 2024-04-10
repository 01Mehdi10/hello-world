from tkinter import *
# procédure générale de déplacement :
def avance(gd, hb):
 global x1, y1
 x1, y1 = x1 +gd, y1 +hb
 can1.coords(oval1, x1,y1, x1+30,y1+30)
# gestionnaires d'événements :
def depl_gauche():
 avance(-10, 0)
def depl_droite():
 avance(10, 0)
def depl_haut():
 avance(0, -10)
def depl_bas():
 avance(0, 10)
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 50, 50  # coordonnées initiales
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=600,width=600)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
can1.grid(column=1,columnspan=4)
Button(fen1,text='Haut',command=depl_haut,width=3).grid(column=3,row=1)
Button(fen1,text='Gauche',command=depl_gauche,width=3).grid(column=2,row=2)
Button(fen1,text='Droite',command=depl_droite,width=3).grid(column=4,row=2)
Button(fen1,text='Bas',command=depl_bas,width=3).grid(column=3,row=3)
Button(fen1,text='Quitter',command=fen1.quit).grid()
# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()