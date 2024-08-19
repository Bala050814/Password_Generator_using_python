import tkinter as tk
import random
import string

def strong_pwd(length):
    password=""
    samp_pwd=string.ascii_letters +"!@#$%^&*"+"1234567890"
    for i in range(length):
        password+=random.choice(samp_pwd)
    return password

def medium_pwd():
     #length=int(input("Enter the Length : "))
     password=""
     samp_pwd=string.ascii_letters +"!@#$%^&*"+"1234567890"
     for pwd in range(8):
        password+=random.choice(samp_pwd)
     return password

def simple_pwd():
     #length=int(input("Enter the Lenght of the Password : "))
     password=""
     str1=string.ascii_letters+"1234567890"
     for pwd in range(4):
        password+=random.choice(str1)
     return password

def generated_password():
    choice= var_choice.get()#123

    if choice==1:
        try:
            length=int(entry_length.get())
            password = strong_pwd(length)
        except ValueError:
            password=("Invalid length. Please enter a valid number.")

    elif choice==2:
        password=medium_pwd()
    elif choice==3:
        password=simple_pwd()
    else:
        password="Invalid choice"

    entry_password.config(state=tk.NORMAL)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    entry_password.config(state=tk.DISABLED)

root=tk.Tk()
root.title("Password Generator")
tk.Label(root, text="Password Length (for Strong Password):").grid(row=2, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=2, column=1, padx=20, pady=20)

var_choice = tk.IntVar()
tk.Radiobutton(root, text="Strong Password (Custom Length)", variable=var_choice, value=1).grid(row=3, columnspan=2, padx=10, pady=5)

tk.Radiobutton(root, text="Medium-Level Password (8 Characters)", variable=var_choice, value=2).grid(row=4, columnspan=2, padx=10, pady=5)
tk.Radiobutton(root, text="Simple-Level Password (4 Characters)", variable=var_choice, value=3).grid(row=5, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Generate Password", command=generated_password).grid(row=6, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Generated Password:").grid(row=7, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, state=tk.NORMAL, width=50)
entry_password.grid(row=7, column=1, padx=10, pady=10)


root.mainloop()



          