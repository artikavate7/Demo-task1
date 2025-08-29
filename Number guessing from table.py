import tkinter as tk
from tkinter import messagebox
import random

def new_game():
    global number, table_num
    try:
        table_num = int(table_var.get())
    except ValueError:
        messagebox.showerror("Invalid", "Enter a valid table number!")
        return
    
    # generate random number from 1 to 100
    number = random.randint(1, 100)
    status_var.set(f"Is {number} in the table of {table_num}?")

def check_answer(is_yes):
    global number, table_num
    if table_num == 0:
        messagebox.showwarning("Error", "Start a game first!")
        return
    
    # Check if number is in the table
    in_table = (number % table_num == 0)
    
    if (is_yes and in_table) or (not is_yes and not in_table):
        messagebox.showinfo("Correct!", f"✅ Yes, you got it right!")
    else:
        messagebox.showerror("Wrong!", f"❌ Wrong! {number} is "
                             f"{'in' if in_table else 'not in'} the table of {table_num}.")
    new_game()  # start next round

# --- Tkinter setup ---
root = tk.Tk()
root.title("Table Guessing Game")
root.resizable(False, False)

frame = tk.Frame(root, padx=15, pady=15)
frame.grid()

# Enter table number
tk.Label(frame, text="Enter Table (e.g. 3):").grid(row=0, column=0, sticky="w")
table_var = tk.StringVar(value="3")
tk.Entry(frame, textvariable=table_var, width=6).grid(row=0, column=1, padx=5)

tk.Button(frame, text="New Game", command=new_game).grid(row=0, column=2, padx=5)

# Status label
status_var = tk.StringVar(value="Enter a table number and click 'New Game'")
tk.Label(frame, textvariable=status_var, fg="blue").grid(row=1, column=0, columnspan=3, pady=10)

# Buttons for Yes/No
tk.Button(frame, text="Yes", width=10, command=lambda: check_answer(True)).grid(row=2, column=0, pady=8)
tk.Button(frame, text="No", width=10, command=lambda: check_answer(False)).grid(row=2, column=2, pady=8)

root.mainloop()
