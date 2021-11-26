from tkinter import *

Janela = Tk()

Janela.title('Primeiro App')

Janela.geometry('500x300+300+250')

# Alterar Font Family, Tamanho e Formato
label_1 = Label(text='Esta é a Label 1',
                bg='#2BFA3D',
                font='Arial 20 italic',
                width=400)
label_1.pack()

#Alterar Cor
label_2 = Label(text='Esta é a Label 2',
                bg='#2458FF',
                font='Arial 20 italic',
                fg='#FF598A',
                width=400)
label_2.pack()

Janela.mainloop()
