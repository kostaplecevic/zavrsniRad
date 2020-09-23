from tkinter import *
import pravljenje_predmeta

top = Tk()
top.title("Second window")
global lista_temp
lista_temp = []
predmet_profesor = pravljenje_predmeta.predmet_profesor

ucionice = [
    '1',
    '2',
    '3',
    '4'
]

clicked4 = StringVar()
clicked4.set(ucionice[0])

clicked5 = StringVar()
clicked5.set(predmet_profesor[0])

def dodaj():
    lista.delete(0, END)
    lista_temp.append(clicked5.get() + '       ' + clicked4.get())

    for row in lista_temp:
        lista.insert(END, row)

def selektovano():
    global ovo
    ovo = lista.get(lista.curselection())
    print(ovo)
    label = Label(top, text=ovo)
    label.grid(row=95)
    return ovo

def slanje_predmeta():
    global predmet_profesor
    predmet_profesor = pravljenje_predmeta.predmet_profesor
    drop_predmet_profesor = OptionMenu(top, clicked5, *predmet_profesor)
    drop_predmet_profesor.grid(row=0, column=4)

drop_ucionica = OptionMenu(top, clicked4, *ucionice)
drop_ucionica.grid(row=0, column=3)
drop_predmet_profesor = OptionMenu(top, clicked5, *predmet_profesor)
drop_predmet_profesor.grid(row=0, column=4)

lista = Listbox(top)
lista.grid(row=99)

btn = Button(top, text='Dodaj', command=lambda: dodaj())
btn.grid(row=9)
btn2 = Button(top, text="Close window", command=top.destroy)
btn2.grid(row=10)
b = Button(top, text="Delete", command=lambda lista=lista: lista.delete(ANCHOR))
b.grid(row=11)

b_pravljenje = Button(top, text='Pravljenje', command=lambda: slanje_predmeta())
b_pravljenje.grid(row=12)

