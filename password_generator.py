from tkinter import *
from tkinter import messagebox
from random import randint

def new_rand():
    pw_entry.delete(0, END)
    pw_length_str = length_entry.get()

    try:
        pw_length = int(pw_length_str)
    except ValueError:
        messagebox.showerror("Eroare", "Insereaza un numar.")
        return

    password = ''
    for _ in range(pw_length):
        password += chr(randint(33, 126))
    pw_entry.insert(0, password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

root = Tk()
root.title("Password Generator")
root.geometry("500x250")

password_length_frame = LabelFrame(root, text="Cate caractere doresti sa aiba parola?", font=("Adobe", 10))
password_length_frame.pack(pady=15, padx=15, side=TOP)

length_entry = Entry(password_length_frame, font=("Adobe", 12))
length_entry.grid(row=0, column=1, padx=5, pady=5)

pw_entry = Entry(root, text="", font=("Adobe", 12), bd=0, bg="systembuttonface")
pw_entry.pack(pady=15)

button_frame = Frame(root)
button_frame.pack(pady=15)

generate_button = Button(button_frame, text="Genereaza Parola", font=("Adobe", 12), command=new_rand)
generate_button.grid(row=0, column=0, padx=10)

copy_button = Button(button_frame, text="Copiaza", font=("Adobe", 12), command=clipper)
copy_button.grid(row=0, column=1, padx=10)

root.mainloop()
