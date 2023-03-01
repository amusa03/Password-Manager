# ---------------------------- SAVE PASSWORD------------------------------- #
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def all_websites():
    website_list=[]
    with open("data.json") as file:
        try:
            data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found")
        else:
            for website in data:
                website_list.append(website)
            websites = "\n".join(website_list)
            messagebox.showinfo(title="All Stored Websites",message=websites)



def find_password():
    website = website_entry.get()
    with open("data.json") as file:
        try:
            data = json.load(file)
        except FileNotFoundError:
            messagebox.askokcancel(title="Error",message="No Data File Found")
        else:
            try:
                if data[website]:
                    password = data[website]["password"]
                    messagebox.showinfo(title=website, message=f"Website:{website}\nPassword:{password}")
            except KeyError:
                messagebox.askokcancel(title="Invalid Website",message="No details for the website exists.")



def gen_password():
    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for number in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)

    pyperclip.copy(password)
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }

    if len(website) ==0 or len(password) ==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except:
                with open("data.json", "w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)

                with open("data.json","w") as file:
                    json.dump(data,file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)


window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(70,100,image=logo)
canvas.grid(column=1,row=0)

website_text = Label(text="Website:",font=("courier"))
website_text.grid(row=1,column=0)


email_text = Label(text="Email/Username:",font=("courier"))
email_text.grid(row=2,column=0)

password_text = Label(text="Password:",font=("courier"))
password_text.grid(row=3,column=0)

website_entry = Entry(width=25)
website_entry.grid(column=1,row=1)
website_entry.focus()


email_entry = Entry(width=44)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"amusa03@outlook.com")

password_entry = Entry(width=25)
password_entry.grid(column=1,row=3)

add_button = Button(width=37,text="Add",bg="WHITE",command=save)
add_button.grid(column=1,row=4,columnspan=2)

generate_button = Button(width=15,text="Generate Password",bg="WHITE",command=gen_password)
generate_button.grid(column=2,row=3)

search_button = Button(width=15,text="Search",bg="WHITE",command = find_password)
search_button.grid(column=2,row=1)

website_button = Button(width=15,text="Show All Websites",bg="YELLOW",command = all_websites)
website_button.grid(column=0,row=6)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #




window.mainloop()