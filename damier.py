from tkinter import *
def rang(y,y1,color):
    c = 0
    x = 10
    x1 = 110
    while c < len(color):
        can.create_rectangle(x,y,x1,y1,fill=color[c])
        x += 100
        x1 += 100
        c += 1
        
def damier():
    c = 1
    y = 10
    y1 = 110
    color1 = ['blue','white','blue','white','blue','white','blue','white','blue','white']
    color2 = ['white','blue','white','blue','white','blue','white','blue','white','blue']
    while c < 11:
        if c % 2 == 0:
            color = color2
        if c % 2 != 0:
            color = color1
        rang(y,y1,color)
        y += 100
        y1 += 100
        c += 1
        
##### Programme principal #####
fen = Tk()
can = Canvas(fen, width=1020, height=1020, bg='white')
can.pack(side=TOP, padx=5, pady=5)
b1 = Button(fen, text='Damier',command=damier)
b1.pack(side=LEFT, padx=3, pady=3)
b2 = Button(fen, text='Pions')
b2.pack(side=RIGHT, padx=3, pady=3)
fen.mainloop()