import tkinter as tk
from tkinter import ttk, Scrollbar, CENTER


class Product:
    def __init__(self, tab):
        self.tab = tab
        self.productview()
        self.productlabels()
        self.productaction()

    def productview(self):
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
        tab1_tree['columns'] = ("ID", "Name", "Description",
                                "Type", "Catagory", "Model", "Manufacturer", "Date")

        # Format our columns
        tab1_tree.column("#0", width=0, stretch=0)
        tab1_tree.column("ID",  stretch=0, anchor=CENTER, width='50')
        tab1_tree.column("Name",  stretch=1, anchor='w', width='140')
        tab1_tree.column("Description", stretch=1, anchor=CENTER, width='140')
        tab1_tree.column("Type",  stretch=1, anchor=CENTER, width='100')
        tab1_tree.column("Catagory",  stretch=1, anchor=CENTER, width='100')
        tab1_tree.column("Model",  stretch=1, anchor=CENTER, width='100')
        tab1_tree.column("Manufacturer", stretch=1, anchor=CENTER, width='100')
        tab1_tree.column("Date", stretch=1, anchor=CENTER, width='100')

        # Create our Heading
        tab1_tree.heading("#0", text="", anchor=CENTER)
        tab1_tree.heading("ID", text="ID", anchor=CENTER)
        tab1_tree.heading("Name", text="Name", anchor=CENTER)
        tab1_tree.heading("Description", text="Description", anchor=CENTER)
        tab1_tree.heading("Type", text="Type", anchor=CENTER)
        tab1_tree.heading("Catagory", text="Catagory", anchor=CENTER)
        tab1_tree.heading("Model", text="Model", anchor=CENTER)
        tab1_tree.heading("Manufacturer", text="Manufacturer", anchor=CENTER)
        tab1_tree.heading("Date", text="Date", anchor=CENTER)

        # Add fake data
        data = [['10', 'Hati Traders', 'Balck Socket', 'Socket',
                '2-PIN', 'Top', 'Havels', '10-10-21']]

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

    def productlabels(self):
        # Widgets under tab 1
        lb = ttk.LabelFrame(self.tab, text="Vendor Details")
        lb.grid(row=1, column=0, sticky='ew')
        # tab1_label.grid_rowconfigure(0, weight=1)
        # tab1_label.grid_columnconfigure(0, weight=1)

        lb_id = tk.Label(lb, text="ID", width=20)
        e_id = tk.Entry(lb, width=50)
        lb_name = tk.Label(lb, text="Name", width=20)
        e_name = tk.Entry(lb, width=50)
        lb_desc = tk.Label(lb, text="Description", width=20)
        e_desc = tk.Entry(lb, width=50)
        lb_type = tk.Label(lb, text="Type", width=20)
        e_type = tk.Entry(lb, width=50)
        lb_cat = tk.Label(lb, text="Catagory", width=20)
        e_cat = tk.Entry(lb, width=50)
        lb_model = tk.Label(lb, text="Model", width=20)
        e_model = tk.Entry(lb, width=50)
        lb_manuf = tk.Label(lb, text="Manufacturer", width=20)
        e_manuf = tk.Entry(lb, width=50)
        lb_date = tk.Label(lb, text="Date", width=20)
        e_date = tk.Entry(lb, width=50)

        lb_id.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        e_id.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        lb_name.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        e_name.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        lb_desc.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        e_desc.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        lb_type.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        e_type.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        lb_cat.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        e_cat.grid(row=0, column=3, padx=10, pady=10, sticky='ew')
        lb_model.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
        e_model.grid(row=1, column=3, padx=10, pady=10, sticky='ew')
        lb_manuf.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
        e_manuf.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
        lb_date.grid(row=3, column=2, padx=10, pady=10, sticky='ew')
        e_date.grid(row=3, column=3, padx=10, pady=10, sticky='ew')

    def productaction(self):
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
