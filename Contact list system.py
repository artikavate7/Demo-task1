import tkinter as tk
from tkinter import ttk, messagebox

contacts = []  # list to store contacts as (name, phone)

def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Please enter both Name and Phone!")
        return
    
    contacts.append((name, phone))
    update_list()
    name_var.set("")
    phone_var.set("")
    status_var.set(f"Added contact: {name}")

def delete_contact():
    try:
        selection = contact_list.curselection()[0]
        contact = contacts.pop(selection)
        update_list()
        status_var.set(f"Deleted contact: {contact[0]}")
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a contact to delete!")

def update_list():
    contact_list.delete(0, tk.END)
    for name, phone in contacts:
        contact_list.insert(tk.END, f"{name} - {phone}")

# ---- Tkinter Window ----
root = tk.Tk()
root.title("Contact List System")
root.geometry("600x400")   # BIG window
root.resizable(False, False)

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

# Input fields
ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
name_var = tk.StringVar()
ttk.Entry(frame, textvariable=name_var, width=30).grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Phone:").grid(row=1, column=0, sticky="w", pady=5)
phone_var = tk.StringVar()
ttk.Entry(frame, textvariable=phone_var, width=30).grid(row=1, column=1, pady=5)

# Buttons
ttk.Button(frame, text="Add Contact", command=add_contact).grid(row=2, column=0, pady=10)
ttk.Button(frame, text="Delete Selected", command=delete_contact).grid(row=2, column=1, pady=10)

# Contact List
contact_list = tk.Listbox(frame, width=50, height=12)
contact_list.grid(row=3, column=0, columnspan=2, pady=10)

# Status bar
status_var = tk.StringVar(value="Welcome to Contact List System!")
ttk.Label(frame, textvariable=status_var, foreground="blue").grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
