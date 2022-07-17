from cgitb import text
from re import X
import tkinter as tk
from tkinter import CENTER, RIGHT, TOP, Y, Frame, Scrollbar, ttk
from turtle import bgcolor, width
import dbconnect

# Connect to Database
# conn = dbconnect.dbconnect()
# conn.connect()

# Initialize App
window = tk.Tk()
window.title("Invento | PowerHouse ")
window.minsize(width=600, height=400)
window.state('zoomed')

window.grid_rowconfigure(0, weight=1)  # this needed to be added
window.grid_columnconfigure(0, weight=1)  # as did this

# Main Container
container = tk.Frame(window)
container.grid(row=0, column=0, sticky='nsew')
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)


# Add the Container for tab
tabcontainer = ttk.Notebook(container)
tabcontainer.grid(row=0, column=0, sticky='nsew')
tabcontainer.grid_rowconfigure(0, weight=1)
tabcontainer.grid_columnconfigure(0, weight=1)

tab1 = tk.Frame(tabcontainer)
tab2 = tk.Frame(tabcontainer)

tab1.grid(row=0, column=0, sticky='nsew')
tab2.grid(row=0, column=0, sticky='nsew')

tab1.grid_rowconfigure(0, weight=1)
tab1.grid_columnconfigure(0, weight=1)

tabcontainer.add(tab1, text="Vendor")
tabcontainer.add(tab2, text="Product")

# Widgets under tab 1
tab1_label = ttk.LabelFrame(tab1, text="Vendor Details")
tab1_label.grid(row=1, column=0, sticky='ew')
# tab1_label.grid_rowconfigure(0, weight=1)
# tab1_label.grid_columnconfigure(0, weight=1)

t1_lb_name = tk.Label(tab1_label, text="Name", width=20)
t1_e_name = tk.Entry(tab1_label, width=50)
t1_lb_add = tk.Label(tab1_label, text="Address", width=20)
t1_e_add = tk.Entry(tab1_label, width=50)
t1_lb_city = tk.Label(tab1_label, text="City", width=20)
t1_e_city = tk.Entry(tab1_label, width=50)
t1_lb_state = tk.Label(tab1_label, text="State", width=20)
t1_e_state = tk.Entry(tab1_label, width=50)
t1_lb_pin = tk.Label(tab1_label, text="PIN", width=20)
t1_e_pin = tk.Entry(tab1_label, width=50)
t1_lb_mob = tk.Label(tab1_label, text="Mobile", width=20)
t1_e_mob = tk.Entry(tab1_label, width=50)
t1_lb_email = tk.Label(tab1_label, text="Email", width=20)
t1_e_email = tk.Entry(tab1_label, width=50)

# adding button to tab1
tab1_button = ttk.LabelFrame(tab1, text="Actions")
tab1_button.grid(row=2, column=0, sticky='nsew')
# tab1_button.grid_rowconfigure(0, weight=1)
# tab1_button.grid_columnconfigure(0, weight=1)
t1_btn_add = tk.Button(tab1_button, text='Add',
                       width=10, bg="green", fg="white")
t1_btn_update = tk.Button(tab1_button, text='Update',
                          width=10, bg="yellow")
t1_btn_del = tk.Button(tab1_button, text='Delete',
                       width=10, bg="red", fg="white")

t1_lb_name.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
t1_e_name.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
t1_lb_add.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
t1_e_add.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
t1_lb_city.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
t1_e_city.grid(row=0, column=3, padx=10, pady=10, sticky='ew')
t1_lb_state.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
t1_e_state.grid(row=1, column=3, padx=10, pady=10, sticky='ew')
t1_lb_pin.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
t1_e_pin.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
t1_lb_mob.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
t1_e_mob.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
t1_lb_email.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
t1_e_email.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

t1_btn_add.grid(row=0, column=0, padx=10, pady=10, sticky='w')
t1_btn_update.grid(row=0, column=1, padx=10, pady=10, sticky='w')
t1_btn_del.grid(row=0, column=2, padx=10, pady=10, sticky='w')

# Add Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the TreView Colours
style.configure('Treeview',
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3"
                )

# Chnage Selected Colour
style.map('Treeview',
          background=[('selected', "#347083")]
          )

# Create a treeview Frame
tab1_list = ttk.LabelFrame(tab1, text='List of Vendors')
tab1_list.grid(row=0, column=0, sticky='nsew')
tab1_list.grid_rowconfigure(0, weight=1)
tab1_list.grid_columnconfigure(0, weight=1)
# Create a Listbox scrollbar
tab1_list_scroll = Scrollbar(tab1_list)
tab1_list_scroll.grid(row=0, column=1, sticky='w')

# Create the Treeview
tab1_tree = ttk.Treeview(
    tab1_list, yscrollcommand=tab1_list_scroll.set, selectmode="extended")
tab1_tree.grid(row=0, column=0, sticky='nsew')
tab1_list.grid_columnconfigure(0, weight=1)

# Configure the ScrolBar
tab1_list_scroll.config(command=tab1_tree.yview)

# Define Our Columns
tab1_tree['columns'] = ("ID", "Name", "Address", "City",
                        'State', 'Pin', "Mobile", "Email")

# Format our columns
tab1_tree.column("#0", width=0, stretch=0)
tab1_tree.column("ID",  stretch=0, anchor=CENTER, width='50')
tab1_tree.column("Name",  stretch=1, anchor='w', width='140')
tab1_tree.column("Address", stretch=1, anchor=CENTER, width='140')
tab1_tree.column("City",  stretch=1, anchor=CENTER, width='100')
tab1_tree.column("State",  stretch=1, anchor=CENTER, width='100')
tab1_tree.column("Pin",  stretch=1, anchor=CENTER, width='100')
tab1_tree.column("Mobile", stretch=1, anchor=CENTER, width='100')
tab1_tree.column("Email", stretch=1, anchor=CENTER, width='100')

# Create our Heading
tab1_tree.heading("#0", text="", anchor=CENTER)
tab1_tree.heading("ID", text="ID", anchor=CENTER)
tab1_tree.heading("Name", text="Name", anchor=CENTER)
tab1_tree.heading("Address", text="Address", anchor=CENTER)
tab1_tree.heading("City", text="City", anchor=CENTER)
tab1_tree.heading("State", text="State", anchor=CENTER)
tab1_tree.heading("Pin", text="PIN", anchor=CENTER)
tab1_tree.heading("Mobile", text="Mobile", anchor=CENTER)
tab1_tree.heading("Email", text="Email", anchor=CENTER)

# Add fake data
data = [['10', 'Sriram', '2/11 vivekananda', 'durgapur',
         'WB', '713204', '9987577095', 'biplab@gmail.com']]

# Create Striped Rows
tab1_tree.tag_configure('oddrow', background='white')
tab1_tree.tag_configure('evenrow', background='lightblue')

# add our data to the screen
global count
count = 0

for record in data:
    if count % 2 == 0:
        tab1_tree.insert(parent="", index="end", iid=count, text="", values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
    else:
        tab1_tree.insert(parent="", index="end", iid=count, text="", values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))
    count += 1

window.mainloop()
