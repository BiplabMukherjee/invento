import tkinter as tk
from tkinter import Frame, ttk
import dbconnect

# Connect to Database
conn = dbconnect.dbconnect()
conn.connect()

# Initialize App
window = tk.Tk()
window.title("Invento | PowerHouse ")
window.minsize(width=500, height=400)

# Main Container
container = tk.Frame(window)
container.pack(expand=True, fill="both")

# Add the Tabs
tabcontainer = ttk.Notebook(container)
tabcontainer.pack(expand=True, fill="both")
tab1 = tk.Frame(tabcontainer, bg='blue')
tab2 = tk.Frame(tabcontainer, bg="red")

tab1.pack(expand=True, fill="both")
tab2.pack(expand=True, fill="both")

tabcontainer.add(tab1, text="Add Vendor")
tabcontainer.add(tab2, text="Add Product")

# Widgets under tab 1
lb_name = tk.Label(tab1, text="Name")
e_name = tk.Entry(tab1)

lb_name.grid(row=0, column=0, padx=10, pady=10)
e_name.grid(row=0, column=1, padx=10, pady=10)


window.mainloop()
