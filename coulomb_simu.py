from tkinter import *
# procédure générale de déplacement :
def avance_lune(event):
 global x1, y1
 x1, y1 = event.x, event.y
 can1.coords(oval1, x1-15,y1-15, x1+15,y1+15)
 distance_terre_lune_soleil()
 
def avance_terre(event):
 global x2, y2
 x2, y2 = event.x, event.y
 can1.coords(oval2, x2-15,y2-15, x2+15,y2+15)
 distance_terre_lune_soleil()
 
 
def distance_terre_lune_soleil():
 global ech
 D_tl = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5,2) # distance terre/lune
 
 D_sl = round(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5,2) # distance soleil/lune
 
 D_st = round(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5,2) # distance soleil/terre
 
 Fg_tl = G * (p_terre * p_lune)/D_tl**2
 Fg_tl = round(Fg_tl,2) # force gravitationnelle terre/lune
 
 Fg_sl = G * (p_soleil * p_lune)/D_sl**2
 Fg_sl = round(Fg_sl,2) # force gravitationnelle soleil/lune
 
 Fg_st = G * (p_soleil * p_terre)/D_st**2
 Fg_st = round(Fg_st,2) # force gravitationnelle soleil/terre

 if D_tl < (15/4 + 15/4):  # Si les astres se chevauchent
   e_astres.config(text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance terre/lune : 0 km \n Force G terre/lune : \n' + str(Fg_tl)+
                 '\n Force G soleil/lune : \n' + str(Fg_sl)+'\n Force G soleil/terre : \n' + str(Fg_st)) # échelle de distance, distance entre les astres, force gravitationnelle
 else:
   D_tl = round(D_tl * ech, 2)
   e_astres.config(text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance terre/lune : ' + str(D_tl) + ' km \n Force G terre/lune : \n' + str(Fg_tl)+
                 '\n Force G soleil/lune : \n' + str(Fg_sl)+'\n Force G soleil/terre : \n' + str(Fg_st)) # échelle de distance, distance entre les astres, force gravitationnelle
    
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
    
ech = 384400/400 # calcul échelle de distance

x1, y1 = 200, 200  # coordonnées initiales de la lune
x2, y2 = 250,250 # coordonnées initiales de la terre
x3, y3 = 150, 200  # coordonnées initiales du soleil

# Calcul distance de la terre à la lune
D_tl = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5,2)
D_tl = D_tl * ech

# Calcul distance du soleil à la lune
D_sl = round(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5,2)
D_sl = D_sl * ech

# Calcul distance du soleil à la terre
D_st = round(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5,2)
D_st = D_st * ech

# masses de la terre, de la lune et du soleil        
p_terre, p_lune, p_soleil = 5.972 * 10 ** 24,  7.342 * 10 ** 22, 1.989 * 10 ** 15

G = 8.9875 * 10 ** 9 # constante de la gravitation

Fg_tl = G * (p_terre * p_lune)/(D_tl/ech)**2
Fg_tl = round(Fg_tl,2) # force gravitationnelle terre/lune

Fg_sl = G * (p_soleil * p_lune)/(D_sl/ech)**2
Fg_sl = round(Fg_sl,2) # force gravitationnelle soleil/lune

Fg_st = G * (p_soleil * p_terre)/(D_st/ech)**2
Fg_st = round(Fg_st,2) # force gravitationnelle soleil/lune

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
###
### création des widgets "esclaves" :
###    

can1 = Canvas(fen1,bg='dark grey',height=300,width=300) 
can1.grid(column=0,row=2)# Canvas

# oval3 = can1.create_oval(x3-15,y3-15,x3+15,y3+15,width=2,fill='orange') 

oval1 = can1.create_oval(x1-15,y1-15,x1+15,y1+15,width=2,fill='yellow') # charge 2

oval2 = can1.create_oval(x2-15,y2-15,x2+15,y2+15,width=2,fill='blue') # charge 3

e_astres = Label(fen1,text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance terre/lune : ' + str(D_tl) +
                 ' km \n Force éléctrostatique : \n' + str(Fg_tl)) # Label du bas qui affiche l'échelle de distance, distance entre les astres, forces gravitationnelles
e_astres.grid(column=0,row=3)

#sep2 = Label(fen1,text='\n')
#sep2.grid(column=0,row=4)

# Boutons lune
def b_lune():
    can1.bind("<Button-1>", avance_lune)
    can1.grid()
Button(fen1,text='Charge 2',command=b_lune,width=5).grid(column=0,row=5,pady=20)

#sep1 = Label(fen1,text='\n')
#sep1.grid(column=0,row=6,pady=10)

# Bouton terre
def b_terre():
    can1.bind("<Button-1>", avance_terre)
    can1.grid()
Button(fen1,text='Charge 1',command=b_terre,width=5).grid(column=0,row=6,pady=20)

Button(fen1,text='Quitter',command=fen1.destroy).grid(sticky=SW)

# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()