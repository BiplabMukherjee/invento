import tkinter as tk
from tkinter import END, ttk, Scrollbar, CENTER

from setuptools import Command
from dbconnect import Dbconnect


class Product:
    def __init__(self, tab):
        self.tab = tab
        self.productview()
        self.productlabels()
        self.productaction()
        self.db = Dbconnect()
        self.dbconn = self.db.connect()
        # creating a cursor to perform a sql operation
        self.c = self.dbconn.cursor()

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
        tab_list = ttk.LabelFrame(self.tab, text='List of Vendors')
        tab_list.grid(row=0, column=0, sticky='nsew')
        tab_list.grid_rowconfigure(0, weight=1)
        tab_list.grid_columnconfigure(0, weight=1)

        # Create a Listbox scrollbar
        tab_list_scroll = Scrollbar(tab_list)
        tab_list_scroll.grid(row=0, column=1, sticky='w')

        # Create the Treeview
        self.tab_tree = ttk.Treeview(
            tab_list, yscrollcommand=tab_list_scroll.set, selectmode="extended")
        self.tab_tree.grid(row=0, column=0, sticky='nsew')
        tab_list.grid_columnconfigure(0, weight=1)

        # Configure the ScrolBar
        tab_list_scroll.config(command=self.tab_tree.yview)

        # Define Our Columns
        self.tab_tree['columns'] = ("ID", "Name", "Description",
                                    "Type", "Catagory", "Model", "Manufacturer", "Date")

        # Format our columns
        self.tab_tree.column("#0", width=0, stretch=0)
        self.tab_tree.column("ID",  stretch=0, anchor=CENTER, width='50')
        self.tab_tree.column("Name",  stretch=1, anchor='w', width='140')
        self.tab_tree.column("Description", stretch=1,
                             anchor=CENTER, width='140')
        self.tab_tree.column("Type",  stretch=1, anchor=CENTER, width='100')
        self.tab_tree.column("Catagory",  stretch=1,
                             anchor=CENTER, width='100')
        self.tab_tree.column("Model",  stretch=1, anchor=CENTER, width='100')
        self.tab_tree.column("Manufacturer", stretch=1,
                             anchor=CENTER, width='100')
        self.tab_tree.column("Date", stretch=1, anchor=CENTER, width='100')

        # Create our Heading
        self.tab_tree.heading("#0", text="", anchor=CENTER)
        self.tab_tree.heading("ID", text="ID", anchor=CENTER)
        self.tab_tree.heading("Name", text="Name", anchor=CENTER)
        self.tab_tree.heading("Description", text="Description", anchor=CENTER)
        self.tab_tree.heading("Type", text="Type", anchor=CENTER)
        self.tab_tree.heading("Catagory", text="Catagory", anchor=CENTER)
        self.tab_tree.heading("Model", text="Model", anchor=CENTER)
        self.tab_tree.heading(
            "Manufacturer", text="Manufacturer", anchor=CENTER)
        self.tab_tree.heading("Date", text="Date", anchor=CENTER)

        # Add fake data
        """ data = [['10', 'Hati Traders', 'Balck Socket', 'Socket',
                '2-PIN', 'Top', 'Havels', '10-10-21']] """

        data = self.getalldata()

        # Create Striped Rows
        self.tab_tree.tag_configure('oddrow', background='white')
        self.tab_tree.tag_configure('evenrow', background='lightblue')

        # add our data to the screen
        global count
        count = 0

        for record in data:
            if count % 2 == 0:
                self.tab_tree.insert(parent="", index="end", iid=count, text="", values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                self.tab_tree.insert(parent="", index="end", iid=count, text="", values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))
            count += 1

        self.tab_tree.bind("<ButtonRelease-1>", self.selectdata)

    def productlabels(self):
        # Widgets under tab 1
        lb = ttk.LabelFrame(self.tab, text="Vendor Details")
        lb.grid(row=1, column=0, sticky='ew')
        # tab1_label.grid_rowconfigure(0, weight=1)
        # tab1_label.grid_columnconfigure(0, weight=1)

        self.lb_id = tk.Label(lb, text="ID", width=20)
        self.e_id = tk.Entry(lb, width=50)
        self.lb_name = tk.Label(lb, text="Name", width=20)
        self.e_name = tk.Entry(lb, width=50)
        self.lb_desc = tk.Label(lb, text="Description", width=20)
        self.e_desc = tk.Entry(lb, width=50)
        self.lb_type = tk.Label(lb, text="Type", width=20)
        self.e_type = tk.Entry(lb, width=50)
        self.lb_cat = tk.Label(lb, text="Catagory", width=20)
        self.e_cat = tk.Entry(lb, width=50)
        self.lb_model = tk.Label(lb, text="Model", width=20)
        self.e_model = tk.Entry(lb, width=50)
        self.lb_manuf = tk.Label(lb, text="Manufacturer", width=20)
        self.e_manuf = tk.Entry(lb, width=50)
        self.lb_date = tk.Label(lb, text="Date", width=20)
        self.e_date = tk.Entry(lb, width=50)

        self.lb_id.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.e_id.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        self.lb_name.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.e_name.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self.lb_desc.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        self.e_desc.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        self.lb_type.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        self.e_type.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self.lb_cat.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        self.e_cat.grid(row=0, column=3, padx=10, pady=10, sticky='ew')
        self.lb_model.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
        self.e_model.grid(row=1, column=3, padx=10, pady=10, sticky='ew')
        self.lb_manuf.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
        self.e_manuf.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
        self.lb_date.grid(row=3, column=2, padx=10, pady=10, sticky='ew')
        self.e_date.grid(row=3, column=3, padx=10, pady=10, sticky='ew')

    def productaction(self):
        # adding button Frame
        action_button = ttk.LabelFrame(self.tab, text="Actions")
        action_button.grid(row=2, column=0, sticky='nsew')

        # Adding Button
        btn_add = tk.Button(action_button, text='Add',
                            width=10, bg="green", fg="white", command=self.insertdata)
        btn_update = tk.Button(action_button, text='Update',
                               width=10, bg="yellow")
        btn_del = tk.Button(action_button, text='Delete',
                            width=10, bg="red", fg="white")
        btn_clear = tk.Button(action_button, text='Clear',
                              width=10, bg="white", fg="black", command=self.cleardata)

        btn_add.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        btn_update.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        btn_del.grid(row=0, column=2, padx=10, pady=10, sticky='w')
        btn_clear.grid(row=0, column=3, padx=10, pady=10,
                       sticky='w')

    def selectdata(self, e):
        # Clear the Entry Area from zeroth position to End
        self.e_id.delete(0, END)
        self.e_name.delete(0, END)
        self.e_desc.delete(0, END)
        self.e_type.delete(0, END)
        self.e_cat.delete(0, END)
        self.e_model.delete(0, END)
        self.e_manuf.delete(0, END)
        self.e_date.delete(0, END)

        # Grab record Number
        selected = self.tab_tree.focus()

        # Grab the record Values
        values = self.tab_tree.item(selected, 'values')

        # Insert the values into the entry Box
        self.e_id.insert(0, values[0])
        self.e_name.insert(0, values[1])
        self.e_desc.insert(0, values[2])
        self.e_type.insert(0, values[3])
        self.e_cat.insert(0, values[4])
        self.e_model.insert(0, values[5])
        self.e_manuf.insert(0, values[6])
        self.e_date.insert(0, values[7])

    def cleardata(self):
        # Clear the Entry Area from zeroth position to End
        self.e_id.delete(0, END)
        self.e_name.delete(0, END)
        self.e_desc.delete(0, END)
        self.e_type.delete(0, END)
        self.e_cat.delete(0, END)
        self.e_model.delete(0, END)
        self.e_manuf.delete(0, END)
        self.e_date.delete(0, END)

    def insertdata(self):
        data = [(
            self.e_id.get(),
            self.e_name.get(),
            self.e_desc.get(),
            self.e_type.get(),
            self.e_cat.get(),
            self.e_model.get(),
            self.e_manuf.get(),
            self.e_date.get(),
        )]
        # sql query
        query = '''
        INSERT INTO `product` (`id`, `pid`, `name`, `des`, `type`, `catagory`, `model`, `manuf`, `date`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);
        '''
        # execute the command
        self.c.executemany(query, data)
        # commit the changes
        self.dbconn.commit()
        print('{} records inserted'.format(self.c.rowcount))

    def getalldata(self):
        # Query
        query = '''SELECT * FROM `product`;'''
        # execute the command
        self.c.execute(query)
        records = self.c.fetchall()
        return records
