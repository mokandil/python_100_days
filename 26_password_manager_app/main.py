import tkinter as tk
import random
import string
import os
from PIL import Image, ImageTk

# get the name of the current directory
current_dir = os.path.dirname(__file__)
data_file = os.path.join(current_dir, "data.txt")
logo_file = os.path.join(current_dir, "logo.png")


class PasswordManager:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Manager")
        self.window.minsize(width=300, height=300)
        self.window.config(padx=50, pady=50)

        # Create and add logo
        # read and resize image
        self.logo = Image.open(logo_file)
        self.logo = self.logo.resize((180, 180))
        self.logo = ImageTk.PhotoImage(self.logo)

        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.grid(column=1, row=0, columnspan=1, pady=20)
        # self.logo_label.config(padx=20, pady=30)

        # Create and add website input field and label
        self.website_label = tk.Label(text="Website:")
        self.website_label.grid(column=0, row=1)
        self.website_entry = tk.Entry(width=52)
        self.website_entry.grid(column=1, row=1, columnspan=2, pady=5)
        self.website_entry.focus()

        # Create and add email/username input field and label
        self.email_label = tk.Label(text="Email/Username:")
        self.email_label.grid(column=0, row=2)
        self.email_entry = tk.Entry(width=52)
        self.email_entry.grid(column=1, row=2, columnspan=2, pady=5)
        self.email_entry.insert(0, "default@example.com")

        # Create and add password input field, label, and generate button
        self.password_label = tk.Label(text="Password:")
        self.password_label.grid(column=0, row=3)
        self.password_entry = tk.Entry(width=30)
        self.password_entry.grid(column=1, row=3, padx=5, pady=5)

        self.generate_button = tk.Button(text="Generate Password", command=self.generate_password, width=16)
        self.generate_button.grid(column=2, row=3, padx=5)

        # Create and add add button
        self.add_button = tk.Button(text="Add", width=44, command=self.add_credentials)
        self.add_button.grid(column=1, row=4, columnspan=2, pady=5)

        self.window.mainloop()

    # Generate a strong password
    def generate_password(self):
        # Clear previous password entry
        self.password_entry.delete(0, tk.END)

        # Define character sets to generate password from
        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        # Generate password
        password = ''.join(random.choice(letters + numbers + symbols) for _ in range(16))

        # Update password entry field with generated password
        self.password_entry.insert(0, password)

    # Add credentials to file
    def add_credentials(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Write credentials to file
        with open(data_file, mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")

        # Clear input fields after credentials are saved
        self.website_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.website_entry.focus()


if __name__ == "__main__":
    password_manager = PasswordManager()
