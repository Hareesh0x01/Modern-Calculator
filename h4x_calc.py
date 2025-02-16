import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import math

# Function to evaluate the expression
def calculate():
    try:
        expression = entry_var.get()
        result = eval(expression)
        entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function to clear entry
def clear():
    entry_var.set("")

# Function to add text to entry
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Creating main window
root = ttk.Window(themename="darkly")  # Modern dark theme
root.title("💀 Hardcore Calculator 💀")
root.geometry("400x550")

entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Helvetica", 24), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Buttons layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '%', '+'),
    ('sin', 'cos', 'tan', 'sqrt'),
    ('log', '(', ')', 'C'),
    ('**', '=', '', '')
]

# Creating buttons dynamically
for row in buttons:
    frame = ttk.Frame(root)
    frame.pack(fill="both", expand=True)
    
    for char in row:
        if char == "":
            ttk.Label(frame, text="").pack(side="left", expand=True)
            continue

        if char == "=":
            btn = ttk.Button(frame, text=char, command=calculate, bootstyle="success")
        elif char == "C":
            btn = ttk.Button(frame, text=char, command=clear, bootstyle="danger")
        elif char in ["sin", "cos", "tan", "sqrt", "log"]:
            btn = ttk.Button(frame, text=char, command=lambda c=char: press(f"math.{c}("), bootstyle="info")
        else:
            btn = ttk.Button(frame, text=char, command=lambda c=char: press(c), bootstyle="secondary")
        
        btn.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Running the app
root.mainloop()
