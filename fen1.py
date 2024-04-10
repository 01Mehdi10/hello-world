# 1er essai avec tkinter
from tkinter import *
fen1 = Tk()
text1 = Label(fen1,text='Bonjour tout le monde !',fg='red')
text1.pack()
bou1 = Button(fen1,text='quitter',command=fen1.destroy    )
bou1.pack()
fen1.mainloop()