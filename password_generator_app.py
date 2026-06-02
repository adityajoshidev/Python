from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for x in range(nr_letters)]+[random.choice(symbols) for y in range(nr_symbols)]+[random.choice(numbers) for z in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if password=="" or website=="":
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"Email : {email}\n"
                                                           f"Password : {password}\n"
                                                           f"Are you sure?")
        if is_ok:
            toast=Frame(window)
            Label(toast,text="Password saved and \ncopied successfully.",fg="red").pack()
            toast.place(relx=0.90,rely=1,anchor="n")
            window.after(3000,toast.destroy)
            pyperclip.copy(password)
            with open("data.txt",'a') as file:
                file.write(f"{website.capitalize()} | {email} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
canvas=Canvas(height=200,width=200)
window.config(pady=50,padx=50)
window.title("Password Generator")
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry=Entry(width=52)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=52)
email_entry.grid(row=2,columnspan=2,column=1)
email_entry.insert(0,"example@gmail.com")

password_entry=Entry(width=33)
password_entry.grid(row=3,column=1)

generate_button=Button(text="Generate Password",width=15,command=password_generator)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=44,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()
