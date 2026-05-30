from tkinter import *

tk=Tk()
tk.config(pady=20,padx=20)

user_input=Entry(width=7)
user_input.grid(column=1,row=0)

miles=Label(text="Miles")
miles.grid(column=2,row=0)

is_equal_to=Label(text="is equal to")
is_equal_to.grid(column=0,row=1)


show_answer=Label(text=0)
show_answer.grid(column=1,row=1)

km=Label(text="Km")
km.grid(column=2,row=1)

def calculate():
    show_answer.config(text=int(user_input.get())*1.609344)

button=Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)



tk.mainloop()
