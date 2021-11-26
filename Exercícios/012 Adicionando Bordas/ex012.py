from tkinter import *

janela = Tk()

janela.title('Bordas')

janela.geometry('500x300+300+250')

borda_1 = Label(text='Solid',
                font='Arial, 20',
                border=5,
                relief='solid'
)
borda_1.pack()

borda_2 = Label(text='Groove',
                font='Arial, 20',
                border=5,
                relief='groove'
)
borda_2.pack()

borda_3 = Label(text='Flat',
                font='Arial, 20',
                border=5,
                relief='flat'
)
borda_3.pack()

borda_4 = Label(text='Raised',
                font='Arial, 20',
                border=5,
                relief='raised'
)
borda_4.pack()

borda_5 = Label(text='Sunken',
                font='Arial, 20',
                border=5,
                relief='sunken'
)
borda_5.pack()

borda_6 = Label(text='Ridge',
                font='Arial, 20',
                border=5,
                relief='ridge'
)
borda_6.pack()

janela.mainloop()
