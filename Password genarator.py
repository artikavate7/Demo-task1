# Password Generator - Tkinter (works in IDLE)
import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets

def generate():
    try:
        length = int(len_var.get())
    except ValueError:
        messagebox.showerror("Invalid", "Length must be a number.")
        return

    pool = ""
    if use_lower.get(): pool += string.ascii_lowercase
    if use_upper.get(): pool += string.ascii_uppercase
    if use_digits.get(): pool += string.digits
    if use_symbols.get(): pool += "!@#$%&*?-_=+.,:;"  # safer subset

    if not pool:
        messagebox.showwarning("Choose characters", "Select at least one character set.")
        return
    if length <= 0:
        messagebox.showwarning("Invalid length", "Length must be at least 1.")
        return

    pwd = "".join(secrets.choice(pool) for _ in range(length))
    pwd_var.set(pwd)
    status_var.set("Generated ✔")

def copy_pwd():
    p = pwd_var.get()
    if not p:
        messagebox.showinfo("Nothing to copy", "Generate a password first.")
        return
    root.clipboard_clear()
    root.clipboard_append(p)
    root.update()  # keeps clipboard after window closes
    status_var.set("Copied to clipboard 📋")

root = tk.Tk()
root.title("Password Generator")
root.resizable(False, False)
pad = {"padx": 8, "pady": 6}

main = ttk.Frame(root, padding=10)
main.grid()

# Length + options
ttk.Label(main, text="Length:").grid(row=0, column=0, sticky="w", **pad)
len_var = tk.StringVar(value="12")
len_box = ttk.Spinbox(main, from_=4, to=64, textvariable=len_var, width=6)
len_box.grid(row=0, column=1, sticky="w", **pad)

use_lower = tk.BooleanVar(value=True)
use_upper = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

opts = ttk.Frame(main)
opts.grid(row=1, column=0, columnspan=2, sticky="w", **pad)
ttk.Checkbutton(opts, text="lowercase (a-z)", variable=use_lower).grid(row=0, column=0, sticky="w")
ttk.Checkbutton(opts, text="UPPERCASE (A-Z)", variable=use_upper).grid(row=0, column=1, sticky="w")
ttk.Checkbutton(opts, text="digits (0-9)",  variable=use_digits).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(opts, text="symbols (!@#$...)", variable=use_symbols).grid(row=1, column=1, sticky="w")

# Output row
pwd_var = tk.StringVar()
ttk.Label(main, text="Password:").grid(row=2, column=0, sticky="w", **pad)
pwd_entry = ttk.Entry(main, textvariable=pwd_var, width=30)
pwd_entry.grid(row=2, column=1, sticky="w", **pad)

# Buttons + status
btns = ttk.Frame(main)
btns.grid(row=3, column=0, columnspan=2, **pad)
ttk.Button(btns, text="Generate", command=generate).grid(row=0, column=0, padx=6)
ttk.Button(btns, text="Copy", command=copy_pwd).grid(row=0, column=1, padx=6)

status_var = tk.StringVar(value="Ready")
ttk.Label(main, textvariable=status_var, foreground="gray").grid(row=4, column=0, columnspan=2, sticky="w", **pad)

root.mainloop()
