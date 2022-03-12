from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters + password_numbers +password_symbols

    random.shuffle(password_list)
    password="".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get().lower()
    email=email_entry.get()
    password=password_entry.get()
    new_data={website:{
        "email":email,
        "password":password
    }}
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Error", message="Dont Leave fields empty")
    else:
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f"Details Entered:\nEmail:{email}\nPassword:{password}\nIs data Correct")
        try:
            with open("data.json", "r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            # with open("data.json", "r") as data_file:
            #     data=json.load(data_file)
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)


        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


#######################FIND PASSWORD#############################################

def find_password():
    website=website_entry.get().lower()
    if len(website)==0:
        messagebox.showinfo(title="Error",message="Pls Dont leave website field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                # print(data[website]["password"])
                messagebox.showinfo(title="DETAILS",
                                    message=f'Email:{data[website]["email"]}\nPassword:{data[website]["password"]}')
        except KeyError:
            messagebox.showinfo(title="Error", message="No Such Website Data Available")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Pls Create Password first")

##############################################




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#####ADDING LOGO
canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)



website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email:")
email_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"xyz@email.com")
password_entry=Entry(width=17)
password_entry.grid(column=1,row=3)

pass_button=Button(text="Generate Password",command=generate_password)
pass_button.grid(column=2,row=3)

add_button=Button(text="ADD",width=30,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="Search",command=find_password)
search_button.grid(column=3,row=1)


window.mainloop()
