
### Déplacement d'une balle à l'aide
### d'un bouton d'un bord à l'autre
### dans un canva. 

from tkinter import *

# Partie calcules
x = 5
def avance_rond():
    global x1, y1, x
    if x1 == 20:
        x = 5
    if x1 == 385:
        x = - 5
    x1, y1 = x1+x,100
    can.coords(rond,x1-15,y1-15,x1+15,y1+15)
        
# partie principales
##############
x1, y1 = 20, 100

fen = Tk() # widget principal
fen.title('Balade balle')

### widgets esclaves ###

# Canva qui contient le rond qui se déplace
can = Canvas(fen,width=400,height=400,bg='white')
can.grid(column=1,row=1)

#Rond rouge que l'on déplace à l'aide d'un bouton'
rond = can.create_oval(x1-15,y1-15,x1+15,y1+15,width=2,fill='red')

# Bouton pour déplacer le rond
bouton = Button(fen,text='>',command=avance_rond,width=5,bg='white').grid(column=1,row=2,pady=10)

# Bouton pour quitter l'application
Button(fen,text='Quitter',command=fen.destroy,bg='white').grid(sticky=SW)

fen.mainloop()