from tkinter import *

top3 = Tk()
top3.title("Second window")
top3.geometry("200x200")

fond_casova = {}
predmeti = [
    'UIS',
    'Java',
    'OZI']

def dodavanje_casova():
    if clicked7.get() not in fond_casova:
        fond_casova[clicked7.get()] = e.get() + e2.get()
        lista_fondova.delete(0, END)

        for row in fond_casova:
            lista_fondova.insert(END, row)

clicked7 = StringVar()
clicked7.set(predmeti[0])

drop_predmet = OptionMenu(top3, clicked7, *predmeti)
drop_predmet.grid(row=2, column=2)

e = Entry(top3,width=5)
e.grid(row=0,column=0)
e2 = Entry(top3,width=5)
e2.grid(row=1,column=1)

lista_fondova = Listbox(top3)
lista_fondova.grid(row=99)

btn = Button(top3, text='Dodaj casove', command=lambda: dodavanje_casova())
btn.grid(row=99)