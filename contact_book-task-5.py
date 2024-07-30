from tkinter import *
from tkinter import ttk

w1 = Tk()
w1.title ("Contact Book ")
w1.geometry('625x480')
w1.configure(bg = "lavender")  

datas = [] 
 
def add(): 
	global datas 
	datas.append([Name.get(),Number.get(),Email.get(),address.get(1.0, "end-1c")]) 
	update_book() 
 
def view(): 
	Name.set(datas[int(select.curselection()[0])][0]) 
	Number.set(datas[int(select.curselection()[0])][1])
	Email.set(datas[int(select.curselection()[0])][2])
	address.delete(1.0,"end") 
	address.insert(1.0, datas[int(select.curselection()[0])][3]) 

def delete(): 
	del datas[int(select.curselection()[0])] 
	update_book() 

def reset(): 
	Name.set('') 
	Number.set('')
	Email.set('')
	address.delete(1.0,"end") 

def update_book(): 
	select.delete(0,END) 
	for n,p,e,a in datas: 
		select.insert(END, n) 

Name = StringVar() 
Number = StringVar() 
Email = StringVar() 
address = StringVar()


l1 = Label(w1, text = "CONTACT BOOK", font = "Arial 17 bold", fg = "purple", bg = "lavender")
l1.place(x = 170, y = 5)

Label(w1, text = "Name  ", font = "Arial 15", bg = "lavender").place(x = 20, y = 45)
Entry(w1, textvariable = Name, width = 17, bd = 2, font = "Arial 14").place(x = 90, y = 45)

Label(w1, text = "Ph no ", font = "Arial 15", bg = "lavender").place(x = 20, y = 80)
Entry(w1, width = 17, textvariable = Number, bd = 2, font = "Arial 14").place(x = 90, y = 80)

Label(w1, text = "Email ", font = "Arial 15", bg = "lavender").place(x = 20, y = 115)
Entry(w1, width = 17, textvariable = Email, bd = 2, font = "Arial 14").place(x = 90, y = 115)

Label(w1, text = 'Address', font='Arial 15', bg = "lavender").place(x = 15, y = 150) 
address = Text(w1,width=17, height = 1, bd = 2, font = "Arial 14") 
address.place(x = 95, y = 150)

Label(w1, text = "List of contacts: ", font='cambria 18',bg="lavender").place(x=15,y=218)

Button(w1,text="Add",width=20,bg="dark blue",fg="white",font="Arial 15",command=add).place(x = 320, y = 45)

Button(w1,text="View",width=20,bg="dark blue",fg="white",font="Arial 15",command=view).place(x = 320, y = 90)

Button(w1,text="Delete",width=20,bg="dark blue",fg="white",font="Arial 15",command=delete).place(x = 320, y = 135)

Button(w1,text="Reset",width=20,bg="dark blue",fg="white",font="Arial 15",command=reset).place(x = 320, y = 180)
  
scroll_bar = Scrollbar(w1, orient=VERTICAL) 
select =Listbox(w1, yscrollcommand=scroll_bar.set, width = 50, height = 8,font="Arial 15") 
scroll_bar.config (command=select.yview) 
scroll_bar.pack(side=RIGHT, fill=Y) 
select.place(x=20,y=250) 

w1.mainloop()