#hewwo :D   (  'v' )/

from tkinter import *
from tkinter import messagebox
import tempfile
import os

root=Tk()
root.title('Billing Management System')

#size window
root.geometry('1280x720')

#warna background
bg_color='#1B2838'



#Variable variable buat menu
Menua=IntVar()
Menub=IntVar()
Menuc=IntVar()
John=IntVar()
Total=IntVar()

cb=StringVar()
cw=StringVar()
cr=StringVar()
cg=StringVar()
total_cost=StringVar()
# function
def total():
    if Menua.get()==0 and Menub.get()==0 and Menuc.get()==0 and John.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Menua.get()
        w=Menub.get()
        r=Menuc.get()
        g=John.get()

        t=float(b*5.5+w*10.5+r*50+g*98)
        Total.set(b + w + r + g)
        total_cost.set('$ ' + str(round(t, 2)))

        cb.set('$ '+str(round(b * 5.5, 2)))
        cw.set('$ '+str(round(w*10.5,2)))
        cr.set('$ '+str(round(r*50,2)))
        cg.set('$ '+str(round(g*98,2)))






def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END, f"================================")
    textarea.insert(END, f"                     Steam Wallet Cart")
    textarea.insert(END, f"\n       Ini adalah informasi pembelian anda :D")
    textarea.insert(END, f"\n================================")
    textarea.insert(END,' Items\tNumber of Items\t  Cost of Items\n')
    textarea.insert(END,f'\n5 USD\t\t{Menua.get()}\t  {cb.get()}')
    textarea.insert(END,f'\n\n10 USD\t\t{Menub.get()}\t  {cw.get()}')
    textarea.insert(END,f'\n\n50 USD\t\t{Menuc.get()}\t  {cr.get()}')
    textarea.insert(END,f'\n\n100 USD\t\t{John.get()}\t  {cg.get()}')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END,f'\nTotal \t\t{Total.get()}\t{total_cost.get()}')
    textarea.insert(END, f"\n================================")
    textarea.insert(END, f"\n         Please give this to the cashier :D")
    textarea.insert(END, f"\n><><><><><><><><><><><><><><><><")




def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')


def reset():
    textarea.delete(1.0,END)
    Menua.set(0)
    Menub.set(0)
    Menuc.set(0)
    John.set(0)
    Total.set(0)

    cb.set('')
    cw.set('')
    cr.set('')
    cg.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()

title=Label(root,pady=5,text="PURCHASE STEAM WALLET VOUCHER",bd=12,bg=bg_color,fg='white',font=('Motiva Sans', 34 ),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#product details text
F1 = LabelFrame(root, text='Product Details', font=('times new roman', 18, 'bold'), fg='white',bg=bg_color,bd=15,relief=RIDGE)
F1.place(x=5, y=80,width=800,height=500)

#Design heading
itm=Label(F1, text='Add Funds', font=('Helvetic',20, 'bold','underline'), fg='white',bg=bg_color)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1, text='Total of Funds', font=('Helvetic',20, 'bold','underline'), fg='white',bg=bg_color)
n.grid(row=0,column=1,padx=30,pady=15)

cost=Label(F1, text='Cost of Funds', font=('Helvetic',20, 'bold','underline'), fg='white',bg=bg_color)
cost.grid(row=0,column=2,padx=30,pady=15)

#Steam Wallet

menua=Label(F1, text='Add $5', font=('Motiva Sans',20), fg='white',bg=bg_color)
menua.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Menua,justify=CENTER)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cb,justify=CENTER)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

menub=Label(F1, text='Add $10', font=('Motiva Sans',20), fg='white',bg=bg_color)
menub.grid(row=2,column=0,padx=20,pady=15)
w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Menub,justify=CENTER)
w_txt.grid(row=2,column=1,padx=20,pady=15)
cw_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cw,justify=CENTER)
cw_txt.grid(row=2,column=2,padx=20,pady=15)

menuc=Label(F1, text='Add $50', font=('Motiva Sans',20), fg='white',bg=bg_color)
menuc.grid(row=3,column=0,padx=20,pady=15)
r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Menuc,justify=CENTER)
r_txt.grid(row=3,column=1,padx=20,pady=15)
cr_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cr,justify=CENTER)
cr_txt.grid(row=3,column=2,padx=20,pady=15)

john=Label(F1, text='Add $100', font=('Motiva Sans',20), fg='white',bg=bg_color)
john.grid(row=4,column=0,padx=20,pady=15)
g_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=John,justify=CENTER)
g_txt.grid(row=4,column=1,padx=20,pady=15)
cg_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cg,justify=CENTER)
cg_txt.grid(row=4,column=2,padx=20,pady=15)

t=Label(F1, text='Total',font=('Motiva Sans',20), fg='white',bg=bg_color)
t.grid(row=5,column=0,padx=20,pady=15)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Total,justify=CENTER)
t_txt.grid(row=5,column=1,padx=20,pady=15)
totalcost_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=total_cost,justify=CENTER)
totalcost_txt.grid(row=5,column=2,padx=20,pady=15)

#Bill
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text='Your Bill',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)



#tombol
F3 =Frame(root,bg=bg_color,bd=15,relief=RIDGE)
F3.place(x=5, y=590,width=1270,height=120)

btn1 = Button(F3, text='Show Total', font='arial 25 bold', padx=5, pady=5, bg='#5ba32b',fg='white',width=10,command=total)
btn1.grid(row=0,column=0,padx=20,pady=10)

btn2 = Button(F3, text='Show Receipt', font='arial 25 bold', padx=5, pady=5, bg='#5ba32b',fg='white',width=10,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3 = Button(F3, text='Print Receipt', font='arial 25 bold', padx=5, pady=5, bg='#5ba32b',fg='white',width=10,command=print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4 = Button(F3, text='CLEAR', font='arial 25 bold', padx=5, pady=5, bg='#5ba32b',fg='white',width=10,command=reset)
btn4.grid(row=0,column=3,padx=10,pady=10)

btn5 = Button(F3, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='#5ba32b',fg='white',width=10,command=exit)
btn5.grid(row=0,column=4,padx=10,pady=10)





root.mainloop()

