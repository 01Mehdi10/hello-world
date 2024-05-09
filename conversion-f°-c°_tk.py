from tkinter import *
from math import *

# Conversion degrés Fahrenheit et degrés celsius dans 2 champs Entry avec tkinter

# fonction convertion°
def c_f(event):
    
    # Bloquer l'utilisation des touches alphabétiques et autres caractères
    try:
        float(celc.get())
    except:
        if celc.get() == '-':
            t = True
        else:
            t = False
            celc.delete(len(celc.get())-1,'end')
            
    try:
        float(fahr.get())
    except:
        if fahr.get() == '-':
            t = True
        else:
            t = False
            fahr.delete(len(fahr.get())-1,'end') 
            
    # convertion C° à F°
    if fenetre.focus_get() == celc:
        fahr.delete(0,'end')
        if celc.index('end') != 0 and celc.get() != '-':
            fahr.insert(0,str(round(float(celc.get()) * 1.8 + 32,2)))
      
    # convertion F° à C°
    if fenetre.focus_get() == fahr:
        celc.delete(0,'end')
        if fahr.index('end') != 0 and fahr.get() != '-':
            celc.insert(0,str(round((float(fahr.get()) - 32) / 1.8,2)))


# ----- Programme principal : -----
fenetre = Tk()
fenetre.title('Convertion celcius <---> Fahrenheit')

# zone texte celcius
texte_c = Label(fenetre,text='Celcius')
texte_c.grid(column=1,row=1)

# formulaire Celcius
celc = Entry(fenetre)
fenetre.bind("<KeyRelease>", c_f)
celc.grid(column=2,row=1,pady=5)

# zone texte Fahrenheit
texte_f = Label(fenetre,text='Fahrenheit')
texte_f.grid(column=1,row=2)

# formulaire Fahrenheit
fahr = Entry(fenetre)
fahr.grid(column=2,row=2,pady=5)

# Aide
aide = Label(fenetre,text='Entre un nombre dans un des champs de saise.')
aide.grid(column=1,row=3,columnspan=2)

fenetre.mainloop()