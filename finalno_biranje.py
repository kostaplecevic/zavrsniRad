from tkinter import *
#import biranje_ucionice,pravljenje_predmeta,fond_casova

finalno_biranje = Tk()
finalno_biranje.title('Finalno')
finalno_biranje.geometry('400x200')

def postavi():
    return 0

predmeti = ['VEB', 'AROS', 'ENG', 'OO', 'PRED']

predmet = StringVar()
predmet.set(predmeti[0])

l1 = Label(finalno_biranje, text='Ucionica 1')
l2 = Label(finalno_biranje, text='Ucionica 2')
l3 = Label(finalno_biranje, text='Ucionica 3')
l4 = Label(finalno_biranje, text='Ucionica 4')
l5 = Label(finalno_biranje, text='Ucionica 5')
l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=0,column=2)
l4.grid(row=0,column=3)
l5.grid(row=0,column=4)

drop_predmet = OptionMenu(finalno_biranje, predmet, *predmeti)
drop_predmet.grid(row=2)

btn1 = Button(finalno_biranje, text='None', command=lambda: postavi())
btn2 = Button(finalno_biranje, text='None', command=lambda: postavi())
btn3 = Button(finalno_biranje, text='None', command=lambda: postavi())
btn4 = Button(finalno_biranje, text='None', command=lambda: postavi())
btn5 = Button(finalno_biranje, text='None', command=lambda: postavi())

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=1,column=3)
btn5.grid(row=1,column=4)

finalno_biranje.mainloop()