from tkinter import *

janela = Tk()

janela.title('Primeiro App')

janela.geometry('500x300+300+250')

label_1 = Label(text='Label 1')
label_1.pack()

label_2 = Label(text='Label 2')
label_2.pack()

botao = Button(text='Botão')
botao.pack()

janela.mainloop()
