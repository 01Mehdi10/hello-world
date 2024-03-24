from tkinter import *
def damier():
    
##### Programme principal #####
fen = Tk()
can = Canvas(fen, width=800, height=800, bg='white')
can.pack(side=TOP, padx=5, pady=5)
b1 = Button(fen, text='Damier')
b1.pack(side=LEFT, padx=3, pady=3)
b2 = Button(fen, text='Pions')
b2.pack(side=RIGHT, padx=3, pady=3)
fen.mainloop()