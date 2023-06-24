from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols+password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def pass_save():
    web_cont = web_entry.get()
    user_cont = user_entry.get()
    pass_cont = pass_entry.get()
    if len(web_cont) == 0 or len(user_cont) == 0 or len(pass_cont) == 0 :
        messagebox.showinfo(title="Warning",message="Please Don't Leave any of the Fields Empty")
    else:
        is_ok =messagebox.askyesno(title=web_cont,
                            message=f"Website:{web_cont}\n E-Mail:{user_cont}\n Password:{pass_cont}\n Is it Okay to Save")
        if is_ok:
            with open("pass_data.txt",mode="a") as f :
                f.write(f"{web_cont} | {user_cont} | {pass_cont}\n")
            web_entry.delete(0,END)
            pass_entry.delete(0,END)

    # success_label = Label(text="Password Saved Successfully!!")
    # success_label.place(x=130,y=375)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=500,height=500)
window.config(padx=40,pady=40)
canvas = Canvas(width=400,height=400,highlightthickness=0)
sec_image = PhotoImage(file="logo.png")
canvas.create_image(200,120,image=sec_image)
# Entry Widgets
web_entry=Entry()
web_entry.config(width=35)
web_entry.focus()
web_entry.place(x=130,y=250)
user_entry=Entry(width=35)
user_entry.insert(0,string="abc@gmail.com")
user_entry.place(x=130,y=283)
pass_entry = Entry(width=21)
pass_entry.place(x=130,y=313)
# Button Entries
gen_button = Button(width=14,text="Generate Password",command=gen_pass)
gen_button.place(x=270,y=309)
add_button=Button(width=36,text="Add Password",command=pass_save)
add_button.place(x=130,y=343)
# Labels
web_label = Label(text="Website:")
web_label.place(x=70,y=250)
user_label = Label(text="Email/Username:")
user_label.place(x=30,y=283)
pass_label = Label(text="Password:")
pass_label.place(x=60,y=313)

canvas.pack()

window.mainloop()