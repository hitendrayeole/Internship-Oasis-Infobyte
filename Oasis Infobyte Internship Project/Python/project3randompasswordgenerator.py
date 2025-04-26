import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        
        # Create main container
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Password length
        ttk.Label(main_frame, text="Password Length:").pack(anchor=tk.W)
        self.length_entry = ttk.Entry(main_frame)
        self.length_entry.pack(fill=tk.X, pady=5)
        self.length_entry.insert(0, "12")  # Default length
        
        # Character options
        options_frame = ttk.LabelFrame(main_frame, text="Character Types")
        options_frame.pack(fill=tk.X, pady=10)
        
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.upper_var).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.lower_var).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Digits (0-9)", variable=self.digits_var).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Symbols (!@#...)", variable=self.symbols_var).pack(anchor=tk.W)
        
        # Exclude characters
        ttk.Label(main_frame, text="Exclude Characters:").pack(anchor=tk.W)
        self.exclude_entry = ttk.Entry(main_frame)
        self.exclude_entry.pack(fill=tk.X, pady=5)
        
        # Generate button
        ttk.Button(main_frame, text="Generate Password", command=self.generate_password).pack(pady=10)
        
        # Result display
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, 
                                 font=('Courier', 12), state='readonly')
        password_entry.pack(fill=tk.X)
        
        # Copy button
        ttk.Button(main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)
        
    def generate_password(self):
        try:
            # Get password length
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showerror("Error", "Password must be at least 4 characters")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid password length")
            return
            
        # Build character set
        chars = []
        if self.upper_var.get():
            chars += list(string.ascii_uppercase)
        if self.lower_var.get():
            chars += list(string.ascii_lowercase)
        if self.digits_var.get():
            chars += list(string.digits)
        if self.symbols_var.get():
            chars += list("!@#$%^&*()_+-=[]{}|;:,.<>?")
            
        if not chars:
            messagebox.showerror("Error", "Select at least one character type")
            return
            
        # Remove excluded characters
        exclude = self.exclude_entry.get()
        chars = [c for c in chars if c not in exclude]
        
        if not chars:
            messagebox.showerror("Error", "No characters available after exclusion")
            return
            
        # Generate secure password
        while True:
            password = ''.join(secrets.choice(chars) for _ in range(length))
            # Ensure password meets complexity requirements
            if (
                (not self.upper_var.get() or any(c.isupper() for c in password)) and
                (not self.lower_var.get() or any(c.islower() for c in password)) and
                (not self.digits_var.get() or any(c.isdigit() for c in password)) and
                (not self.symbols_var.get() or any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password))
            ):
                break
                
        self.password_var.set(password)
        
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "No password to copy")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
