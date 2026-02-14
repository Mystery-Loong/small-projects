from tkinter import *
from tkinter import ttk
from cryptography.fernet import Fernet

import tkinter as tk
import random
import string


def get_password_info():
    digits_number = digits.get()
    letters_number = letters.get()
    print(f"digits number is: {digits_number}")
    print(f"letters number is: {letters_number}")
    s1 = random.choices(string.digits, k=int(digits_number))
    s2 = random.choices(string.ascii_letters, k=int(letters_number))
    s = s1 + s2
    random.shuffle(s)
    password = ''.join(s)
    print(f"The password is: {password}")
    password_get.set(password)
    encrypted_password(password)
    
def encrypted_password(password):
    # generate password key
    key = generate_or_load_key()
    cipher = Fernet(key)

    # encrypted data
    data = password.encode('utf-8')
    encrypted_data = cipher.encrypt(data)
    print(f"Encrypted data is: {encrypted_data}")
    save_password(encrypted_data)

def save_password(encrypted_data):
    with open('encrypted-password.bin', 'ab') as f:
        f.write(encrypted_data + b'\n')

def display_password():
    # generate password key
    key = generate_or_load_key()
    cipher = Fernet(key)
    with open("encrypted-password.bin", "rb") as f:
        lines = f.readlines()
    print(lines[-1])
    # decrypted data
    decrypted_data = cipher.decrypt(lines[-1])
    print(f"Decrypted data is: {decrypted_data}")
    password_get.set(decrypted_data)

def generate_or_load_key():
    try:
        with open("key_path", "rb") as f:
            key = f.read()
            print(f"Old key is: {key}")
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key_path", "wb") as f:
            f.write(key)
    return key

root = Tk()
root.title("Password Generato")
root.geometry("450x300")

digits = tk.StringVar()
letters = tk.StringVar()
password_get = tk.StringVar()

display_box = tk.Label(
    root, 
    text='Please enter the digits and letters number?',
    font=("Arial", 14, "bold"),
    relief="ridge",
    width=40
    )
display_box.grid(column=0, row=0, columnspan=7, padx=2, pady=2)
digits_display = tk.Label(
    root,
    text='Digits number',
    font=("Arial", 13, "bold"),
    relief="ridge",
    width=19
)
digits_display.grid(column=1, row=2, columnspan=2, padx=2, pady=10)
letters_display = tk.Label(
    root,
    text='Letters number',
    font=("Arial", 13, "bold"),
    relief="ridge",
    width=19
)
letters_display.grid(column=4, row=2, columnspan=2, padx=2, pady=10)
digits_entry_box = tk.Entry(
    root,
    font=("Arial", 16),
    textvariable=digits,
    width=8
)
digits_entry_box.grid(column=1, row=3, columnspan=2, padx=2, pady=5)
letters_entry_box = tk.Entry(
    root,
    font=("Arial", 16),
    textvariable=letters,
    width=8
)
letters_entry_box.grid(column=4, row=3, columnspan=2, padx=2, pady=5)
GeneratePassword = tk.Button(
    root,
    text="Generate new password",
    font=("微软雅黑", 20),
    command=get_password_info
)
GeneratePassword.grid(column=1, row=4, columnspan=5, pady=10)
DisplayPassword = tk.Button(
    root,
    text="Display password",
    font=("微软雅黑", 20),
    command=display_password
)
DisplayPassword.grid(column=1, row=6, columnspan=5, pady=10)
password_display = tk.Entry(
    root,
    textvariable=password_get,
    font=("微软雅黑", 18),
    state="readonly",
    relief="flat"
)
password_display.grid(column=0, row=8, columnspan=9, padx=2, pady=10)


mainloop()