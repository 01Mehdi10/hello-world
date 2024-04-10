# Affichage d'un petit cercle sur clic de souris dans une fenêtre :
from tkinter import *
def pointeur(event):
   r = 15
   chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
            ", Y =" + str(event.y))
   X = event.x
   Y = event.y
   cadre.create_oval(X-r,Y-r,X+r,Y+r,fill='red')
fen = Tk()
cadre = Canvas(fen, width =800, height =800, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()