from multiprocessing import set_forkserver_preload
import tkinter as tk
from tkinter import ttk
from product import Product
from vendor import Vendor


class main():
    def __init__(self, window):
        self.window = window
        self.setwindow()
        self.maincontainer()
        self.addtabs()
        pass

    def setwindow(self):
        self.window.title("Invento | PowerHouse ")
        self.window.minsize(width=600, height=400)
        self.window.state('zoomed')
        self.window.grid_rowconfigure(0, weight=1)  # this needed to be added
        self.window.grid_columnconfigure(0, weight=1)  # as did this

    def maincontainer(self):
        # Main Container
        self.container = tk.Frame(self.window)
        self.container.grid(row=0, column=0, sticky='nsew')
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def addtabs(self):
        # Add the Container for tab
        self.tabcontainer = ttk.Notebook(self.container)
        self.tabcontainer.grid(row=0, column=0, sticky='nsew')
        self.tabcontainer.grid_rowconfigure(0, weight=1)
        self.tabcontainer.grid_columnconfigure(0, weight=1)

        # Create Frame for Tabs
        self.tab1 = tk.Frame(self.tabcontainer)
        self.tab2 = tk.Frame(self.tabcontainer)

        # Pack the Tabs in display
        self.tab1.grid(row=0, column=0, sticky='nsew')
        self.tab2.grid(row=0, column=0, sticky='nsew')

        # Grid configure to to reset the rows and columns inside the Frame
        self.tab1.grid_rowconfigure(0, weight=1)
        self.tab1.grid_columnconfigure(0, weight=1)
        self.tab2.grid_rowconfigure(0, weight=1)
        self.tab2.grid_columnconfigure(0, weight=1)

        # Add the Tabs to Tab container
        self.tabcontainer.add(self.tab1, text="Vendor")
        self.tabcontainer.add(self.tab2, text="Product")

        # Call the Tabs
        Vendor(self.tab1)
        Product(self.tab2)


window = tk.Tk()
app = main(window)
window.mainloop()
