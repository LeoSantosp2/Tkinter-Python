from tkinter import *

janela = Tk()

janela.title('Primeiro App')

janela.geometry('500x300+300+250')

#Altera Cor de Fundo da Janela
janela['bg'] = 'blue'

#Altera Cor de Fundo da Label
label_1 = Label(text='Esta é a Label 1',
                bg='#2BFA3D')
label_1.pack()

label_2 = Label(text='Esta é a Label 2',
                bg='#608BFC')
label_2.pack()

janela.mainloop()
