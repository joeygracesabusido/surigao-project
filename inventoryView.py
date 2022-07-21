from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkcalendar import DateEntry
from tkcalendar import DateEntry as TkcDateEntry
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
import PIL.Image
import datetime as dt

from datetime import date, datetime

from abc import ABC,abstractmethod

class Controller:
    def __init__(self,view):
        self.view = view

    def start(self):
        self.view.set_up(self) 
        self.view.start_main_loop()
        # self.view.inventory_treeview_display()


    def handle_clear_entry_inventory(self):
        self.view.clear_list()

    def insert_inventory(self):
        self.view.insert_inventoryOnhand()
        self.view.inventory_treeview_display()
        self.view.clear_list()
    def display_inventory(self):
        self.view.inventory_treeview_display()

class Inventory():
    """This is for Inventory View"""

    def set_up(self,controller):

        self.root = Tk()
        self.root.title("JRS SYSTEM")
        self.root.geometry("1150x550")
        
        self.root.config(bg="black")
        

        

        self.productID = Label(self.root, text='Product ID:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.productID.place(x=10, y=30)

    
        self.product_id_entry = Entry(self.root, width=15, font=('Arial', 10))
        self.product_id_entry.place(x=150, y=30)

        self.brand_lbl = Label(self.root, text='Brand:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.brand_lbl.place(x=10, y=60)

    
        self.brand_inv = Entry(self.root, width=15, font=('Arial', 10))
        self.brand_inv.place(x=150, y=60)

        self.description_lbl = Label(self.root, text='Description:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.description_lbl.place(x=10, y=90)

        self.descrtip_inv_entry = scrolledtext.ScrolledText(self.root,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
        self.descrtip_inv_entry.place(x=150, y=90)

        self.quanity_lbl = Label(self.root, text='Quantity:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.quanity_lbl.place(x=10, y=150)

        self.quantity_inv = Entry(self.root, width=15, font=('Arial', 10))
        self.quantity_inv.place(x=150, y=150)

        self.price_lbl = Label(self.root, text='Price:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.price_lbl.place(x=10, y=180)

        self.price_inv = Entry(self.root, width=15, font=('Arial', 10))
        self.price_inv.place(x=150, y=180)

        self.unit_lbl = Label(self.root, text='Unit:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.unit_lbl.place(x=10, y=210)

        self.unit_inv = Entry(self.root, width=15, font=('Arial', 10))
        self.unit_inv.place(x=150, y=210)

        self.category_lbl = Label(self.root, text='Category:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.category_lbl.place(x=10, y=240)

        self.categoryEntry = ttk.Combobox(self.root, width=20,font=('Arial', 10))
        self.categoryEntry['values'] = 'Test'
        self.categoryEntry.place(x=150, y=240)
        # self.categoryEntry.bind("<<ComboboxSelected>>", auto_account_num)


        self.btn_save = Button(self.root, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.insert_inventory)
        self.btn_save.place(x=10, y=270)

        self.btn_display = Button(self.root, text='Display', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.display_inventory)
        self.btn_display.place(x=850, y=15)


        self.inventoryTreeview_form = Frame(self.root, width=700, height=10)
        self.inventoryTreeview_form.place(x=380, y=40)

        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=20,
                        fieldbackground="white")
    
        
        
        
        scrollbarx = Scrollbar(self.inventoryTreeview_form, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.inventoryTreeview_form, orient=VERTICAL)
        
        self.inventoryTreeview = ttk.Treeview(self.inventoryTreeview_form,
                                                columns=('Product ID','Brand', 'Description','Quantity',
                                                'Unit','Amount'),
                                                selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                                xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.inventoryTreeview.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.inventoryTreeview.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.inventoryTreeview.heading('Product ID', text="Product ID", anchor=CENTER)
        self.inventoryTreeview.heading('Brand', text="Brand", anchor=CENTER)
        self.inventoryTreeview.heading('Description', text="Descrtiption", anchor=CENTER)
        self.inventoryTreeview.heading('Quantity', text="Quantity", anchor=CENTER)
        self.inventoryTreeview.heading('Unit', text="Unit", anchor=CENTER)
        self.inventoryTreeview.heading('Amount', text="Amount", anchor=CENTER)
         


        self.inventoryTreeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
        self.inventoryTreeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='center')
        self.inventoryTreeview.column('#2', stretch=NO, minwidth=0, width=70, anchor='sw')
        self.inventoryTreeview.column('#3', stretch=NO, minwidth=0, width=150, anchor='sw')
        self.inventoryTreeview.column('#4', stretch=NO, minwidth=0, width=150, anchor='e')
        self.inventoryTreeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
        self.inventoryTreeview.column('#6', stretch=NO, minwidth=0, width=100, anchor='e')
        
       
    
        self.inventoryTreeview.pack()

        # if userName_entry_registry.get() != 'joeysabusido':
        #     self.btn_save['state'] = DISABLED
        


    def clear_list(self): # this is to clear all fields
        self.product_id_entry.delete(0,END)
        self.brand_inv.delete(0,END)
        self.descrtip_inv_entry.delete('1.0', END)
        self.price_inv.delete(0, END)
        self.quantity_inv.delete(0, END)
        self.categoryEntry.delete(0, END)
        self.unit_inv.delete(0, END)
    
    
    
    def insert_inventoryOnhand(self): # this is to insert record 
        """This function is for inserting to inventory On hand"""
        today = date.today()
        from inventory_database import Database
       
        
        Database.initialize()

        productID_Insert = self.product_id_entry.get()
        brand_inv_Insert = self.brand_inv.get()
        description_insert = self.descrtip_inv_entry.get('1.0', 'end-1c')
        quantity_insert = self.quantity_inv.get()
        price_insert = self.price_inv.get()
        categoryInsert = self.categoryEntry.get()
        unitInsert = self.unit_inv.get()
          
        date_insert = today

        data = Database.select_Inventory(productID_Insert)

        if data is not None:
            messagebox.showinfo('JRS','Equipment ID is already Taken')
        else:
            if productID_Insert =='' or brand_inv_Insert=='' or description_insert=='' \
                or quantity_insert==''or price_insert=="":
                messagebox.showinfo('Please fill up  blank entry field/s ')
            else:
                try:
                    Database.insert_inventoryOnhand(product_id=productID_Insert,brand=brand_inv_Insert,
                                                    description=description_insert,quantity=quantity_insert,
                                                    price=price_insert,date=date_insert,category=categoryInsert,
                                                    unit=unitInsert)
                    
                    messagebox.showinfo('JRS','Data has been save')
                except Exception as ex:
                    messagebox.showerror( f"Error due to :{str(ex)}")

    def inventory_treeview_display(self):
        self.inventoryTreeview.delete(*self.inventoryTreeview.get_children())
        return self.inventory_treevie_list()

    def inventory_treevie_list(self):
        """This function is for querying for treeview for inventory Database"""
        from inventory_database import Database
        Database.initialize()   

        myresult = Database.select_all_from_inventoryData()

        for i in myresult:
            self.productID_view = i[1]   
            self.brand_view = i[2]   
            self.description_view = i[3]  
            self.quantity_view = i[4] 
            self.unit_view = i[6]
            self.stockamount_view ='{:,.2f}'.format(i[7])

            self.inventoryTreeview.insert('', 'end', values=(self.productID_view,self.brand_view,
                                self.description_view,self.quantity_view,self.unit_view,self.stockamount_view))
        

    def start_main_loop(self):

        self.root.mainloop()


# c = Controller(Inventory())
# c.start()

