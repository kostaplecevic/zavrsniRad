from tkinter import *
def app():
    root = Tk()
    root.title("Raspored")
    #root.iconbitmap("")
    #root.geometry("400x400")

    profesori = [
        "Mika",
        "Tijana",
        "Bolovic",
        "Ana",
    ]
    predmeti = ['UIS','Java','OZI']

    clicked2 = StringVar()
    clicked2.set(profesori[0])

    clicked3 = StringVar()
    clicked3.set(predmeti[0])

    drop = OptionMenu(root, clicked2, *profesori)
    drop.grid(row=0,column=1)
    drop2 = OptionMenu(root, clicked3, *predmeti)
    drop2.grid(row=0, column=2)

    def doit(x):
        #clicked.set(clicked2.get())
        if x=='pon1':
            pon1.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon2':
            pon2.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon3':
            pon3.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon4':
            pon4.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon5':
            pon5.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon6':
            pon6.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon7':
            pon7.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon8':
            pon8.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon9':
            pon9.configure(text=clicked2.get()+"-"+clicked3.get())
        elif x == 'pon10':
            pon10.configure(text=clicked2.get()+"-"+clicked3.get())

    ucionica0 = Label(root, text='Ucionice/Vreme')
    ucionica1 = Label(root, text='1')
    ucionica2 = Label(root, text='2')
    ucionica3 = Label(root, text='3')
    ucionica4 = Label(root, text='4')
    ucionica5 = Label(root, text='5')
    vreme1 = Label(root, text='9.00')
    vreme2 = Label(root, text='10.00')
    vreme3 = Label(root, text='11.00')
    vreme4 = Label(root, text='12.00')
    vreme5 = Label(root, text='13.00')


    pon1 = Button(root, text='None', width=10, command=lambda: doit('pon1'))

    pon2 = Button(root, text='None', width=10, command=lambda: doit('pon2'))

    pon3 = Button(root, text='None', width=10, command=lambda: doit('pon3'))

    pon4 = Button(root, text='None', width=10, command=lambda: doit('pon4'))

    pon5 = Button(root, text='None', width=10, command=lambda: doit('pon5'))

    pon6 = Button(root, text='None', width=10, command=lambda: doit('pon6'))

    pon7 = Button(root, text='None', width=10, command=lambda: doit('pon7'))

    pon8 = Button(root, text='None', width=10, command=lambda: doit('pon8'))

    pon9 = Button(root, text='None', width=10, command=lambda: doit('pon9'))

    pon10 = Button(root, text='None', width=10, command=lambda: doit('pon10'))

    ucionica0.grid(row=1, column=0)
    ucionica1.grid(row=2, column=0)
    ucionica2.grid(row=3, column=0)
    ucionica3.grid(row=4, column=0)
    ucionica4.grid(row=5, column=0)
    ucionica5.grid(row=6, column=0)
    vreme1.grid(row=1, column=1)
    vreme2.grid(row=1, column=2)
    vreme3.grid(row=1, column=3)
    vreme4.grid(row=1, column=4)
    vreme5.grid(row=1, column=5)

    pon1.grid(row=2, column=1)
    pon2.grid(row=3, column=1)
    pon3.grid(row=4, column=1)
    pon4.grid(row=5, column=1)
    pon5.grid(row=6, column=1)
    pon6.grid(row=2, column=2)
    pon7.grid(row=3, column=2)
    pon8.grid(row=4, column=2)
    pon9.grid(row=5, column=2)
    pon10.grid(row=6, column=2)

    root.mainloop()

app()