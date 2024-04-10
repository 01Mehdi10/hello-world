from tkinter import *
# procédure générale de déplacement :
def avance_lune(event):
 global x1, y1
 x1, y1 = event.x, event.y
 can1.coords(oval1, x1-30,y1-30, x1+30,y1+30)
 distance_terre_lune_soleil()
 
def avance_terre(event):
 global x2, y2
 x2, y2 = event.x, event.y
 can1.coords(oval2, x2-80,y2-80, x2+80,y2+80)
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

 if D_tl < (80/4 + 30/4):  # Si les astres se chevauchent
   e_astres.config(text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance terre/lune : 0 km \n Force G terre/lune : \n' + str(Fg_tl)+' N'+
                 '\n Force G soleil/lune : \n' + str(Fg_sl)+' N'+'\n Force G soleil/terre : \n' + str(Fg_st)+' N') # échelle de distance, distance entre les astres, force gravitationnelle
 else:
   D_tl = round(D_tl * ech, 2)
   e_astres.config(text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance terre/lune : ' + str(D_tl) + ' km \n Force G terre/lune : \n' + str(Fg_tl)+ ' N' +
                 '\n Force G soleil/lune : \n' + str(Fg_sl)+' N'+'\n Force G soleil/terre : \n' + str(Fg_st)+ ' N') # échelle de distance, distance entre les astres, force gravitationnelle
    
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
    
ech = 384400/400 # calcul échelle de distance

x1, y1 = 200, 200  # coordonnées initiales de la lune
x2, y2 = 350,350 # coordonnées initiales de la terre
x3, y3 = 500, 100  # coordonnées initiales du soleil

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
p_terre, p_lune, p_soleil = 5.972 * 10 ** 24,  7.342 * 10 ** 22, 1.989 * 10 ** 30

G = 6.674*10**-11 # constante de la gravitation

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
m_astres = Label(fen1,text='Masse de la terre = ' + str(p_terre)+'\n Masse de la lune ='+str(p_lune) +'\n Masse du soleil = '+str(p_soleil)) #m_astres est le label du haut qui affiche la masse des astres
m_astres.grid(column=0,row=1)

can1 = Canvas(fen1,bg='dark grey',height=600,width=600) 
can1.grid(column=0,row=2)# Canvas

oval3 = can1.create_oval(x3-15,y3-15,x3+15,y3+15,width=2,fill='orange') # soleil

oval1 = can1.create_oval(x1-30,y1-30,x1+30,y1+30,width=2,fill='yellow') # lune

oval2 = can1.create_oval(x2-80,y2-80,x2+80,y2+80,width=2,fill='blue') #terre

e_astres = Label(fen1,text='Échelle de distance : \n' + '1 px = ' + str(round(ech, 2)) + ' km' + '\n Distance terre/lune : ' + str(D_tl) +
                 ' km \n Force G terre/lune : \n' + str(Fg_tl)+ ' N' +
                 '\n Force G soleil/lune : \n' + str(Fg_sl)+ ' N' +
                 '\n Force G soleil/terre : \n' + str(Fg_st) + ' N')  # Label du bas qui affiche l'échelle de distance, distance entre les astres, forces gravitationnelles
e_astres.grid(column=0,row=3)

# Boutons lune
def b_lune():
    can1.bind("<Button-1>", avance_lune)
    can1.grid()
Button(fen1,text='Lune',command=b_lune,width=3).grid(column=0,row=5,pady=20)


# Bouton terre
def b_terre():
    can1.bind("<Button-1>", avance_terre)
    can1.grid()
Button(fen1,text='Terre',command=b_terre,width=3).grid(column=0,row=6,pady=20)

Button(fen1,text='Quitter',command=fen1.destroy).grid(sticky=SW)

# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()