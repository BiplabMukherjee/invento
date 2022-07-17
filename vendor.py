import tkinter as tk
from tkinter import ttk, Scrollbar, CENTER


class Vendor:
    def __init__(self, tab):
        self.tab = tab
        self.vendorview()
        self.vendorlabels()
        self.vendoraction()

    def vendorview(self):
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
        tab1_list = ttk.LabelFrame(self.tab, text='List of Vendors')
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

    def vendorlabels(self):
        # Widgets under tab 1
        lb = ttk.LabelFrame(self.tab, text="Vendor Details")
        lb.grid(row=1, column=0, sticky='ew')
        # tab1_label.grid_rowconfigure(0, weight=1)
        # tab1_label.grid_columnconfigure(0, weight=1)

        lb_name = tk.Label(lb, text="Name", width=20)
        e_name = tk.Entry(lb, width=50)
        lb_add = tk.Label(lb, text="Address", width=20)
        e_add = tk.Entry(lb, width=50)
        lb_city = tk.Label(lb, text="City", width=20)
        e_city = tk.Entry(lb, width=50)
        lb_state = tk.Label(lb, text="State", width=20)
        e_state = tk.Entry(lb, width=50)
        lb_pin = tk.Label(lb, text="PIN", width=20)
        e_pin = tk.Entry(lb, width=50)
        lb_mob = tk.Label(lb, text="Mobile", width=20)
        e_mob = tk.Entry(lb, width=50)
        lb_email = tk.Label(lb, text="Email", width=20)
        e_email = tk.Entry(lb, width=50)

        lb_name.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        e_name.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        lb_add.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        e_add.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        lb_city.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        e_city.grid(row=0, column=3, padx=10, pady=10, sticky='ew')
        lb_state.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
        e_state.grid(row=1, column=3, padx=10, pady=10, sticky='ew')
        lb_pin.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
        e_pin.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
        lb_mob.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        e_mob.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        lb_email.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        e_email.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    def vendoraction(self):
        # adding button to tab1
        action_button = ttk.LabelFrame(self.tab, text="Actions")
        action_button.grid(row=2, column=0, sticky='nsew')
        # tab1_button.grid_rowconfigure(0, weight=1)
        # tab1_button.grid_columnconfigure(0, weight=1)
        btn_add = tk.Button(action_button, text='Add',
                            width=10, bg="green", fg="white")
        btn_update = tk.Button(action_button, text='Update',
                               width=10, bg="yellow")
        btn_del = tk.Button(action_button, text='Delete',
                            width=10, bg="red", fg="white")

        btn_add.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        btn_update.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        btn_del.grid(row=0, column=2, padx=10, pady=10, sticky='w')
