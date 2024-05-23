# Cercles et courbes de Lissajous
from tkinter import *
from math import sin, cos
def lissajous(event=None): # marche
    marche('lissajous')
def cercle(event=None):
    marche('cercle')
def marche(forme): #mise en marche
    global en_marche, f
    en_marche=True
    f = forme
    move()
    
def arret(event=None):
    global en_marche
    en_marche=False
def move():
  global ang, x, y
  if en_marche:
  # on mémorise les coordonnées précédentes avant de calculer les nouvelles :
      xp, yp = x, y
  # rotation d'un angle de 0.1 radian :
      ang = ang +.1
  # sinus et cosinus de cet angle => coord. d'un point du cercle trigono.
      if f == "cercle":
          x, y = sin(ang), cos(ang)
  # Variante déterminant une courbe de Lissajous avec f1/f2 = 2/3 :
      if f == "lissajous":
          x, y = sin(2*ang), cos(3*ang)
  # mise à l'échelle (120 = rayon du cercle, (150,150) = centre du canevas
      x, y = x*120 + 150, y*120 + 150
      can.coords(balle, x-10, y-10, x+10, y+10)
      can.create_line(xp, yp, x, y, fill ="blue")     # trace la trajectoire
      can.after(5,move)
ang, x, y = 0., 150., 270.
en_marche=False
def clear():
    can.delete('all')
fen = Tk()
fen.title('Courbes de Lissajous')
first_label = Label(text="Courbes de Lissajous", fg="white", bg="blue")
first_label.pack(side="top", fill='x')
can = Canvas(fen, width =300, height=300, bg="white")
can.pack()
balle = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
# Lissajous
bouton_lissajous=Button(fen, text='Lissajous', command =arret)
bouton_lissajous.pack(pady=10)
bouton_lissajous.bind('<ButtonPress>',lissajous)
bouton_lissajous.bind('<ButtonRelease>',arret)
# Cercle
bouton_cercle=Button(fen, text='Cercle', command =arret)
bouton_cercle.pack(pady=10)
bouton_cercle.bind('<ButtonPress>',cercle)
bouton_cercle.bind('<ButtonRelease>',arret)
#Effacer le canvas
Button(fen, text='Effacer', command=clear).pack()
# Fermer l'application
Button(fen, text='Quitter', command=fen.destroy).pack(side='left')
fen.mainloop()