# IMPORTS
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_txt = website_entry.get()
    username_txt = username_entry.get()
    password_txt = password_entry.get()

    if len(website_txt) < 1 or len(username_txt) < 1 or len(password_txt) < 1:
        is_unfinished = messagebox.showerror('Error', 'Please do not leave any fields blank.')
    else:
        # Message Box Popup
        is_ok = messagebox.askokcancel(website_txt, f'These are the details entered: \n\n'
                                                    f'Website: {website_txt} \nEmail: {username_txt} \n'
                                                    f'Password: {password_txt} \n\nIs it ok to save?')

        if is_ok:
            with open('passwords.txt', 'a') as passwords_txt:
                print(f'{website_txt} | {username_txt} | {password_txt} (Added!)')
                passwords_txt.write(f'{website_txt} | {username_txt} | {password_txt}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Create Window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_lbl = Label(text='Website: ')
website_lbl.grid(row=1, column=0, sticky='nsew')
username_lbl = Label(text='Email / Username: ')
username_lbl.grid(row=2, column=0, sticky='nsew')
password_lbl = Label(text='Password: ')
password_lbl.grid(row=3, column=0, sticky='nsew')

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
# username_entry.insert(0, 'brandon@gmail.com')
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, sticky='ew')


# Buttons
password_btn = Button(text='Generate', command=generate_pass)
password_btn.grid(row=3, column=2, sticky='ew')
add_btn = Button(text='Add', width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
