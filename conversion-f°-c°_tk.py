from tkinter import *
from math import *

# Conversion degrés Fahrenheit et degrés celsius dans 2 champs Entry avec tkinter

# fonction convertion C° à F°
def c_f(event):
    fahr.delete(0,'end')
    fahr.insert(0,str(round(float(celc.get()) * 1.8 + 32,2)))


# fonction convertion F° à C°
def f_c(event):
    celc.delete(0,'end')
    celc.insert(0,str(round((float(fahr.get()) - 32) / 1.8,2)))


# ----- Programme principal : -----

fenetre = Tk()
fenetre.title('Convertion celcius <---> Fahrenheit')

# zone texte celcius
texte_c = Label(fenetre,text='Celcius')
texte_c.grid(column=1,row=1)

# formulaire Celcius
celc = Entry(fenetre)
celc.bind("<Return>", c_f)
celc.grid(column=2,row=1,pady=5)

# zone texte Fahrenheit
texte_f = Label(fenetre,text='Fahrenheit')
texte_f.grid(column=1,row=2)

# formulaire Fahrenheit
fahr = Entry(fenetre)
fahr.bind("<Return>", f_c)
fahr.grid(column=2,row=2,pady=5)

# Aide
help = Label(fenetre,text='Entre un nombre dans\n un des champs de\n saisie puis valide par la\n touche entrée.')
help.grid(column=2,row=3)

fenetre.mainloop()