from tkinter import END, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox
from generator import generator as create_password
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    random_pass = create_password()
    password_entry.delete(0, END)
    password_entry.insert(0, random_pass)
    # Use pypi package to add to clipboard
    # import pyperclip
    # pyperclip.copy(random_pass)
    # pyperclip.paste() # will paste what's in the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(website_entry.get()) == 0 or len(email_user_entry.get()) ==0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Whoops!", message="Make sure all fields are filled out")
        return
    is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"Confirm\nEmail:{email_user_entry.get()}\nPassword:{password_entry.get()}")

    if is_ok:
        with open("data.txt", "a") as data:
            data.write(f"{website_entry.get()} | {email_user_entry.get()} | {password_entry.get()}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
LOCK_IMAGE = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=LOCK_IMAGE)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:").grid(column=0, row=1)
email_user_label = Label(text="Email/Username:").grid(column=0, row=2)
password_label = Label(text="Password:").grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "myemail@mail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate", width=10, command=generate_password).grid(column=2, row=3)
save_pass_button = Button(text="Save Password", width=32, command=save_password).grid(column=1, row=4, columnspan=2)



window.mainloop()