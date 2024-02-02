
from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('500x500')
win.title('list box')
win.config(bg='gray')
#===========================================================================
def insert():
    get_name = f'{ent_name.get()}_{ent_family.get()}'
    lst_box.insert(END,get_name)
    ent_name.delete(0,END)
    ent_family.delete(0,END)
    ent_name.focus_set()

def clear():
    ask = messagebox.askquestion('out','do you want to  clear?')
    if ask == 'yes':
        lst_box.delete(0, END)

def delete():
    ask = messagebox.askquestion('delete', 'do you want to delete?')
    if ask == 'yes':
        index = lst_box.curselection()
        lst_box.delete(index)
def fetch():
    index = lst_box.curselection()
    info = lst_box.get(index)
    ent_name.delete(0,END)
    ent_name.insert(0,info)



#===========================================================================

lbl_show = Label(win,text='name:',font='15',bg='gray')
lbl_show.grid(row=0,column=0)

lbl_show = Label(win,text='family:',font='15',bg='gray')
lbl_show.grid(row=1,column=0)

ent_name = Entry(win,border=5)
ent_name.grid(row=0,column=1)

ent_family = Entry(win,border=5)
ent_family.grid(row=1,column=1)

lst_box = Listbox(win,width=50)
lst_box.place(y=100,x=70)

lst_box.insert(0,'python')
lst_box.insert(1,'c++')
lst_box.indert(2 , 'c#')

btn_insert = Button(win,text='insert',width=7,border=8,command=insert)
btn_insert.place(y=300,x=0)

btn_clear = Button(win,text='clear',width=7,border=8,command=clear)
btn_clear.place(y=300,x=70)

btn_delete = Button(win,text='delete',width=7,border=8,command=delete)
btn_delete.place(y=300,x=140)

btn_fetch = Button(win,text='fetch',width=7,border=8,command=fetch)
btn_fetch.place(y=300,x=210)

print('********************************')



win.mainloop()