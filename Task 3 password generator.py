import tkinter as tk
from tkinter import ttk
import random
import string

# Generate password logic
def generate_password():
    length = int(length_entry.get())
    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        password_display.delete(0, tk.END)
        password_display.insert(0, password)

# Copy password
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_display.get())

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x600")
root.configure(bg="#1c1c1c")

# Style setup
style = ttk.Style()
style.theme_use('clam')

# Purple button style
style.configure("Purple.TButton",
                font=("Helvetica", 14),
                foreground="white",
                background="#9b59b6",
                borderwidth=0,
                padding=10)
style.map("Purple.TButton",
          background=[("active", "#884ea0")])

# Heading
heading = tk.Label(root, text="Secure Password", font=("Helvetica", 18, "bold"), fg="purple", bg="#1c1c1c")
heading.pack(pady=(30, 15))  # Space above and below heading

# Password display
password_display = tk.Entry(root, font=("Courier", 22), justify="center", bd=2, relief="solid")
password_display.pack(pady=(0, 30), ipadx=10, ipady=8, fill="x", padx=20)

# Options Frame
options_frame = tk.Frame(root, bg="#1c1c1c")
options_frame.pack(pady=(0, 30))

# Length input
tk.Label(options_frame, text="Password Length:", font=("Helvetica", 14), bg="#1c1c1c", fg="white").grid(row=0, column=0, sticky="w", pady=5)
length_entry = tk.Entry(options_frame, width=5, font=("Helvetica", 14))
length_entry.grid(row=0, column=1, pady=5, padx=10)
length_entry.insert(0, "8")

# Checkboxes
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Include Uppercase", variable=var_upper, bg="#1c1c1c", fg="white", font=("Helvetica", 14), selectcolor="#1c1c1c").grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(options_frame, text="Include Lowercase", variable=var_lower, bg="#1c1c1c", fg="white", font=("Helvetica", 14), selectcolor="#1c1c1c").grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(options_frame, text="Include Digits", variable=var_digits, bg="#1c1c1c", fg="white", font=("Helvetica", 14), selectcolor="#1c1c1c").grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(options_frame, text="Include Symbols", variable=var_symbols, bg="#1c1c1c", fg="white", font=("Helvetica", 14), selectcolor="#1c1c1c").grid(row=4, column=0, columnspan=2, sticky="w")

# Buttons
generate_btn = ttk.Button(root, text="Generate Password", style="Purple.TButton", command=generate_password)
generate_btn.pack(pady=(10, 10), ipadx=10, ipady=5)

copy_btn = ttk.Button(root, text="Copy to Clipboard", style="Purple.TButton", command=copy_to_clipboard)
copy_btn.pack(pady=(0, 20), ipadx=10, ipady=5)

# Run the GUI app
root.mainloop()