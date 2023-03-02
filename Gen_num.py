from tkinter import*
import random as r

def main():
    a = ent1.get()
    b = ent2.get()
    try:
        res.delete(0, END)
        res.insert(0, r.randint(int(a), int(b)))
    except:
        res.insert(0, r.randint(0, 999))
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent1.insert(0, 0)
        ent2.insert(0, 999)

w = Tk()
w.geometry('500x350')
w.resizable(width=0, height=0)
w['bg'] = 'black'
w.title('Дегенератор случайных чисел')

l1 = Label(w, bg='black', font=('Comic Sans MS', 24, 'bold'), fg='red', text='От какого?')
l1.place(x=35, y =-2)

l2 = Label(w, bg='black', font=('Comic Sans MS', 24, 'bold'), fg='red', text='До какого?')
l2.place(x=280, y =-2)

gen = Button(w, text='Сгенерировать', bg='grey', font=('Comic Sans MS', 24, 'bold'), fg='red', relief='flat', command=main)
gen.place(x=125, y =125)

ent1 = Entry(w, font=('Comic Sans MS', 24, 'bold'), fg='red', width=10)
ent1.place(x=25, y =50)
ent1.insert(0, 0)

ent2 = Entry(w, font=('Comic Sans MS', 24, 'bold'), fg='red', width=10)
ent2.place(x=270, y =50)
ent2.insert(0, 999)

res = Entry(w, font=('Comic Sans MS', 54, 'bold'), fg='red', text=r.randint(0, 999), width=10)
res.place(x=30, y =225)
res.insert(0, r.randint(0, 999))

w.mainloop()
