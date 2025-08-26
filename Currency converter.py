import tkinter as tk
from tkinter import ttk, messagebox

# Fixed exchange rates (for demo purpose)
exchange_rates = {
    "USD": 1.0,       # Base currency
    "INR": 83.2,      # 1 USD = 83.2 INR
    "EUR": 0.92,      # 1 USD = 0.92 EUR
    "GBP": 0.79,      # 1 USD = 0.79 GBP
    "JPY": 146.7      # 1 USD = 146.7 JPY
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_combo.get()
        to_currency = to_combo.get()

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            messagebox.showerror("Error", "Invalid currency selected!")
            return

        # Convert to USD first, then to target currency
        usd_amount = amount / exchange_rates[from_currency]
        converted = usd_amount * exchange_rates[to_currency]

        result_label.config(text=f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# GUI Window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x250")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="💱 Currency Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Amount input
frame1 = tk.Frame(root)
frame1.pack(pady=5)
tk.Label(frame1, text="Amount:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
amount_entry = tk.Entry(frame1, font=("Arial", 12))
amount_entry.grid(row=0, column=1, padx=5)

# From and To currency
frame2 = tk.Frame(root)
frame2.pack(pady=10)

tk.Label(frame2, text="From:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
from_combo = ttk.Combobox(frame2, values=list(exchange_rates.keys()), font=("Arial", 12), state="readonly")
from_combo.current(0)
from_combo.grid(row=0, column=1, padx=5)

tk.Label(frame2, text="To:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
to_combo = ttk.Combobox(frame2, values=list(exchange_rates.keys()), font=("Arial", 12), state="readonly")
to_combo.current(1)
to_combo.grid(row=0, column=3, padx=5)

# Convert Button
convert_btn = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="green", fg="white", command=convert_currency)
convert_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

root.mainloop()
