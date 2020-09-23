
from tkinter import *
import biranje_ucionice
from fond_casova import fond_casova


def app():
    root = Tk()
    root.title("Raspored")
    # root.iconbitmap("")
    # root.geometry("400x400")


    def doit(x):
        ono_sto_nam_treba = biranje_ucionice.selektovano()
        fond = fond_casova[ono_sto_nam_treba]
        if x == 'pon1':
            pon1.configure(text=ono_sto_nam_treba)
        elif x == 'pon2':
            pon2.configure(text=ono_sto_nam_treba)
        elif x == 'pon3':
            pon3.configure(text=ono_sto_nam_treba)
        elif x == 'pon4':
            pon4.configure(text=ono_sto_nam_treba)
        elif x == 'pon5':
            pon5.configure(text=ono_sto_nam_treba)
        elif x == 'pon6':
            pon6.configure(text=ono_sto_nam_treba)
        elif x == 'pon7':
            pon7.configure(text=ono_sto_nam_treba)
        elif x == 'pon8':
            pon8.configure(text=ono_sto_nam_treba)
        elif x == 'pon9':
            pon9.configure(text=ono_sto_nam_treba)
        elif x == 'pon10':
            pon10.configure(text=ono_sto_nam_treba)

    ucionica0 = Label(root, text='Vreme/Dan')
    ucionica1 = Label(root, text='Ponedeljak')
    ucionica2 = Label(root, text='Utorak')
    ucionica3 = Label(root, text='Sreda')
    ucionica4 = Label(root, text='Cetvrtak')
    ucionica5 = Label(root, text='Petak')
    vreme1 = Label(root, text='9.00')
    vreme2 = Label(root, text='10.00')
    vreme3 = Label(root, text='11.00')
    vreme4 = Label(root, text='12.00')
    vreme5 = Label(root, text='13.00')

    pon1 = Button(root, text='None', wraplength=80, width=10, height=3,
                  command=lambda: doit('pon1'))

    pon2 = Button(root, text='None', width=10, height=3, command=lambda: doit('pon2'))

    pon3 = Button(root, text='None', width=10, command=lambda: doit('pon3'))

    pon4 = Button(root, text='None', width=10, command=lambda: doit('pon4'))

    pon5 = Button(root, text='None', width=10, command=lambda: doit('pon5'))

    pon6 = Button(root, text='None', width=10, command=lambda: doit('pon6'))

    pon7 = Button(root, text='None', width=10, command=lambda: doit('pon7'))

    pon8 = Button(root, text='None', width=10, command=lambda: doit('pon8'))

    pon9 = Button(root, text='None', width=10, command=lambda: doit('pon9'))

    pon10 = Button(root, text='None', width=10, command=lambda: doit('pon10'))

#Gridovanje
    ucionica0.grid(row=0, column=0)
    ucionica1.grid(row=0, column=1)
    ucionica2.grid(row=0, column=2)
    ucionica3.grid(row=0, column=3)
    ucionica4.grid(row=0, column=4)
    ucionica5.grid(row=0, column=5)
    vreme1.grid(row=1, column=0)
    vreme2.grid(row=2, column=0)
    vreme3.grid(row=3, column=0)
    vreme4.grid(row=4, column=0)
    vreme5.grid(row=5, column=0)

    pon1.grid(row=1, column=1)
    pon2.grid(row=2, column=1)
    pon3.grid(row=3, column=1)
    pon4.grid(row=4, column=1)
    pon5.grid(row=5, column=1)
    pon6.grid(row=1, column=2)
    pon7.grid(row=2, column=2)
    pon8.grid(row=3, column=2)
    pon9.grid(row=4, column=2)
    pon10.grid(row=5, column=2)

    window_button = Button(root, text='Window', command=lambda: exec(open('biranje_ucionice.py').read()))
    window_button.grid(row=7)

    root.mainloop()


app()
