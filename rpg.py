from tkinter import *
import string
import random
import pyperclip

##########     Password Generator     ##########
password_chars = string.ascii_letters + string.digits + string.punctuation

def password_generator():
    password_field.delete(0, END)
    length = int(char_input.get())
    password = "".join([random.choice(password_chars) for _ in range(length)])
    password_field.insert(0, password)
    pyperclip.copy(password)

##########     User Interface     ##########
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="#1A1A1A")

label_title = Label(text="Password Generator",
                    bg="#1A1A1A",
                    fg="#fff",
                    font=("Arial", 35, "bold"))
label_title.grid(row=0, column=0, columnspan=3, pady=30)

label_before_input = Label(text="I want a password with",
                           bg="#1A1A1A",
                           fg="#fff",
                           font=("Arial", 15, "bold"))
label_before_input.grid(row=1, column=0)

char_input = Entry(bg="#FE5B79")
char_input.grid(row=1, column=1)
char_input.insert(0, "12")
char_input.focus()

label_after_input = Label(text="characters.",
                          bg="#1A1A1A",
                          fg="#fff",
                          font=("Arial", 15, "bold"))
label_after_input.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password & Copy to Clipboard",font=("Arial", 9, "bold"),
                                  bg="#FE5B79",
                                  height=4,
                                  width=55,
                                  command=password_generator)
generate_password_button.grid(row=2, column=0, columnspan=3, padx=50, pady=50)

password_field = Entry(bg="#5F5AFF",font=("Arial", 15, "bold"), width=40)
password_field.grid(row=3, column=0, columnspan=3)

window.mainloop()