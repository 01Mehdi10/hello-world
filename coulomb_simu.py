from tkinter import *


# REMARQUE : le changement de signe donne toujours un résultat
# positif puisque c'est une multiplication de 2 nombres négatifs
s = -1 # signe pour calculer la force electrostatique.

# procédure générale de déplacement :
def avance_c1(event):
 global x1, y1
 x1, y1 = event.x, event.y
 can1.coords(oval1, x1-15,y1-15, x1+15,y1+15)
 distance_c1_c2()

def avance_c2(event):
 global x2, y2
 x2, y2 = event.x, event.y
 can1.coords(oval2, x2-15,y2-15, x2+15,y2+15)
 distance_c1_c2()

def change_signe_plus():
    global s
    if s == -1:
        s = 1

def change_signe_moins():
    global s
    if s == 1:
        s = -1

def distance_c1_c2():
 global ech
 D_c1_c2 = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5,2) # distance charge1 -> charge2

 Fe_c1_c2 = G * ((s*vl_charge1) * (s*vl_charge2))/D_c1_c2
 Fe_c1_c2 = round(Fe_c1_c2,2) # force éléctrostatique charge1 -> charge2 

 if D_c1_c2 < (15/4 + 15/4):  # Si les charges se chevauchent
   e_charges.config(text='Échelle : ' + '1 px = ' + str(round(ech, 2)) + ' mm' + '\n Distance : 0 mm \n Force : ' + str(Fe_c1_c2) + ' N') # échelle de distance, distance entre les charges, force éléctrostatique
 else:
   D_c1_c2 = round(D_c1_c2 * ech, 2)
   e_charges.config(text='Échelle :' + '1 px = ' + str(round(ech, 2)) + ' mm' + '\n Distance : ' + str(D_c1_c2) + ' mm \n Force : ' + str(Fe_c1_c2) + ' N') # échelle de distance, distance entre les charges, force éléctrostatique

#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :

ech = 0.01 # calcul échelle de distance

x1, y1 = 200, 200  # coordonnées initiales charge 1
x2, y2 = 220,220 # coordonnées initiales charge 2

# Calcul distance charge1 -> charge2
D_c1_c2 = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5,2)
D_c1_c2 = D_c1_c2 * ech

# Valeurs charge1 et charge2        
vl_charge1, vl_charge2 = 2, 3

G = 8.9875 * 10 ** 9 # constante électrostatique

Fe_c1_c2 = G * (vl_charge1* vl_charge2)/D_c1_c2
Fe_c1_c2 = round(Fe_c1_c2,2) # force électrostatique charge1 -> charge2

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Force électrostatique")
###
### création des widgets "esclaves" :
###    

can1 = Canvas(fen1,bg='dark grey',height=400,width=400) 
can1.grid(column=0,row=1)# Canvas 

oval1 = can1.create_oval(x1-15,y1-15,x1+15,y1+15,width=2,fill='yellow') # charge 1

oval2 = can1.create_oval(x2-15,y2-15,x2+15,y2+15,width=2,fill='blue') # charge 2

e_charges = Label(fen1,text='Échelle : ' + '1 px = ' + str(round(ech, 2)) + ' mm' + '\n Distance : ' + str(D_c1_c2) + ' mm \n Force : ' + str(Fe_c1_c2) + ' N' ) # Label du bas qui affiche l'échelle de distance, distance entre les astres, forces gravitationnelles
e_charges.grid(column=0,row=3)

frame = Frame(fen1)
frame.grid(column=0,row=2)

# Bouton charge1
def b_charge1():
    can1.bind("<Button-1>", avance_c1)
    can1.grid()
Button(frame,text='Charge 1',command=b_charge1,width=5).grid(column=1,row=1,padx=5)

# Bouton charge2
def b_charge2():
    can1.bind("<Button-1>", avance_c2)
    can1.grid()
Button(frame,text='Charge 2',command=b_charge2,width=5).grid(column=2,row=1,padx=5)

# Bouton +
Button(frame,text='+',command=change_signe_plus,width=2).grid(column=3,row=1,padx=5)

# Bouton -
Button(frame,text='-',command=change_signe_moins,width=2).grid(column=4,row=1,padx=5)

# Bouton pour quitter l'application
Button(fen1,text='Quitter',command=fen1.destroy).grid(sticky=SW)

# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()