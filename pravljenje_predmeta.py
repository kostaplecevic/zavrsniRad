from tkinter import *
import fond_casova

top2 = Tk()
top2.title("Second window")
top2.geometry("200x200")

predmet_profesor = ['Ana-OO']

profesori = [
    "Mika",
    "Tijana",
    "Bolovic",
    "Ana",
]
predmeti = [
    'UIS',
    'Java',
    'OZI']

clicked2 = StringVar()
clicked2.set(profesori[0])

clicked3 = StringVar()
clicked3.set(predmeti[0])

def pravljenje():
    global nesto
    nesto = clicked2.get() + '-' + clicked3.get()
    if nesto not in predmet_profesor:
        predmet_profesor.append(nesto)
        print('UBACEN')
    lista_predmet_profesora.delete(0, END)

    for row in predmet_profesor:
        lista_predmet_profesora.insert(END, row)

lista_predmet_profesora = Listbox(top2)
lista_predmet_profesora.grid(row=99)

drop_profesor = OptionMenu(top2, clicked2, *profesori)
drop_profesor.grid(row=0, column=1)
drop_predmet = OptionMenu(top2, clicked3, *predmeti)
drop_predmet.grid(row=0, column=2)

btn = Button(top2, text='Napravi',command=lambda: pravljenje())
btn.grid(row=15)