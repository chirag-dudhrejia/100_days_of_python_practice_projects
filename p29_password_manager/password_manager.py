import json
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import pyperclip

# ------------------------------------------Constants-------------------------------------------------------------
FONT = "Courier"
FILE_NAME = "data.json"

root = Tk()
root.title("Password Manager")
root.config(pady=20, padx=40)

# ------------------------------------------Centering GUI---------------------------------------------------------
screen_width = 730
screen_height = 500
win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()
x = (win_width // 2) - (screen_width // 2)
y = (win_height // 2) - (screen_height // 2)
root.geometry(f"{screen_width}x{screen_height}+{x}+{y}")
root.resizable(False, False)

# ------------------------------------------Icon Setup------------------------------------------------------------
img1 = Image.open("output_onlinepngtools.png")
logo = ImageTk.PhotoImage(img1)
root.wm_iconphoto(False, logo)


def save_credentials():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    data = {}

    new_data = {
        website: {
            "Email": username,
            "Password": password
        }
    }

    if len(website) > 0 and len(username) > 0 and len(password) > 0:
        try:
            with open(FILE_NAME, "r") as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError:
                    pass
                data.update(new_data)
        except FileNotFoundError:
            with open(FILE_NAME, "w"):
                pass
            save_credentials()
        else:
            with open(FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

        website_entry.focus()
    else:
        messagebox.showerror(title="Details empty", message="Fill all the details!")


def password_generator():
    gen_pass.config(text="Re-Generate")
    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_of_letters = random.randint(8, 10)
    number_of_symbols = random.randint(2, 4)
    number_of_digits = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(number_of_letters)]
    password_list += [random.choice(symbols) for _ in range(number_of_symbols)]
    password_list += [random.choice(numbers) for _ in range(number_of_digits)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, string=f"{password}")


#-------------------------------------------Clipboard copy password-----------------------------------------------
def copy_to_clipboard():
    if len(password_entry.get()) > 0:
        pyperclip.copy(password_entry.get())


#-------------------------------------------Search for records using website--------------------------------------
def search_record():
    website = website_entry.get()
    data = {}
    try:
        if len(website) < 1:
            raise Exception("No input found")

        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title="File is empty!",
                             message="File does not have any data.\nStore data first.")
    except FileNotFoundError:
        messagebox.showerror(title="File not exist!", message="File does not exist.\nStore data first.")
    except Exception:
        messagebox.showerror(title="No Input!", message="Website field can not be empty.\nEnter website name.")
    else:
        try:
            email = data[website]["Email"]
            password = data[website]["Password"]
        except KeyError:
            messagebox.showwarning(title="No data!", message=f"Details for {website} does not exist")
        else:
            messagebox.showinfo(title="Details Found", message=f"Email/Username : {email}\n"
                                                               f"Password            : {password}")


# ------------------------------------------MyPass Image----------------------------------------------------------
canvas = Canvas(width=202, height=202)
img2 = PhotoImage(file="output_onlinepngtools.png")
canvas.create_image(103, 103, image=img2)
canvas.grid(column=0, row=0, columnspan=4, pady=20)

# ------------------------------------------Website Label---------------------------------------------------------
website_label = Label(text="Website:", font=(FONT, 14), width=16)
website_label.grid(column=0, row=1, pady=5)

# ------------------------------------------Website Entry---------------------------------------------------------
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky=NSEW, pady=5)

#-------------------------------------------Search Credentials from file using website name-----------------------
search_button = Button(text="Search", font=(FONT, 14), bg="#b5d7f9", width=20, relief="groove", command=search_record)
search_button.grid(column=3, row=1, padx=(5, 0))

# ------------------------------------------Email / Username Label------------------------------------------------
username_label = Label(text="Email/Username:", font=(FONT, 14), width=16)
username_label.grid(column=0, row=2, pady=5)

# ------------------------------------------Email / Username Entry------------------------------------------------
username_entry = Entry(width=35)
username_entry.insert(0, string="dchirag159@gmail.com")
username_entry.grid(column=1, row=2, columnspan=3, sticky=NSEW, pady=5)

# ------------------------------------------Password Label--------------------------------------------------------
password_label = Label(text="Password:", font=(FONT, 14), width=16)
password_label.grid(column=0, row=3, sticky=NSEW, pady=5)

# ------------------------------------------Password Display------------------------------------------------------
password_entry = Entry(relief="groove", width=30)
password_entry.grid(column=1, row=3, sticky=NSEW, pady=5)

#-------------------------------------------Copy to Clipboard Button----------------------------------------------
image = Image.open("copy.png")
resize_img = image.resize((20, 20))
copy_image = ImageTk.PhotoImage(resize_img)
clipboard = Button(image=copy_image, relief="groove", bg="#C2C2C2", fg="black", command=copy_to_clipboard)
clipboard.grid(column=2, row=3)

# ------------------------------------------Generate Password Button----------------------------------------------
gen_pass = Button(text="Generate Password", font=(FONT, 14), width=20, bg="#b5d7f9", relief="groove", command=password_generator)
gen_pass.grid(column=3, row=3, padx=(5, 0))

# ------------------------------------------Add Credentials Button------------------------------------------------
add_credentials = Button(text="Add", font=(FONT, 14), width=25, bg="#b5d7f9", relief="groove", command=save_credentials)
add_credentials.grid(column=1, row=4, columnspan=3, sticky=NSEW, pady=(10, 0))

# root.attributes("-topmost", 1)
root.mainloop()
