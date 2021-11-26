from tkinter import *

janela = Tk()

janela.title('Primeiro App')

# Dimensões da Tela
largura = 500
altura = 300

#Resolução do Sistema
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

#Posição da Janela
posx = largura_tela / 2 - largura / 2
posy = altura_tela / 2 - altura / 2

janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

janela.mainloop()
