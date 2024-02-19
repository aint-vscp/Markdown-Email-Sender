import tkinter as tk
from tkinter import messagebox
import pyrebase

# Configure Firebase
config = {
    "apiKey": "<apiKey>",
    "authDomain": "<authDomain>",
    "databaseURL": "<databaseURL>",
    "projectId": "<projectId>",
    "storageBucket": "<storageBucket>",
    "messagingSenderId": "<messagingSenderId>",
    "appId": "<appId>",
    "measurementId": "<measurementId>"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def register():
    email = email_entry.get()
    password = password_entry.get()
    try:
        user = auth.create_user_with_email_and_password(email, password)
        messagebox.showinfo("Success", "Registration successful")
    except:
        messagebox.showerror("Error", "Could not register")

def login():
    email = email_entry.get()
    password = password_entry.get()
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        messagebox.showinfo("Success", "Login successful")
    except:
        messagebox.showerror("Error", "Incorrect email or password")

root = tk.Tk()
root.configure(bg='light blue')  # Set the background color of the window

email_label = tk.Label(root, text="Email", bg='light blue')
email_label.pack(pady=10)  # Add some padding
email_entry = tk.Entry(root)
email_entry.pack(pady=10)  # Add some padding

password_label = tk.Label(root, text="Password", bg='light blue')
password_label.pack(pady=10)  # Add some padding
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)  # Add some padding

register_button = tk.Button(root, text="Register", command=register)
register_button.pack(pady=10)  # Add some padding

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)  # Add some padding

root.mainloop()