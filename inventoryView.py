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
import mysql.connector

mydb = mysql.connector.connect(
            host="192.46.225.247",
            user="joeysabusido",
            password="Genesis@11",
            database="ldsurigao",
            auth_plugin='mysql_native_password')
cursor = mydb.cursor()

# def inve_category():
#     """This function is for Displaying inventory category"""
#     # from inventory_database import Database
#     # Database.initialize()
#     # agg_result = Database.select_all_category_from_category()
#     mydb._open_connection()
    
#     cursor.execute('SELECT category FROM category ORDER by category ASC')

#     agg_result = cursor.fetchall()

#     data = []
#     for x in agg_result:
#         data.append(x[0])
#     return data

class Controller:
    def __init__(self,view):
        self.view = view

    def start(self):
        self.view.inve_category()
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
        

        width = 1150
        height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable = False
        
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
        self.categoryEntry['values'] = self.inve_category()
        self.categoryEntry.place(x=150, y=240)
        # self.categoryEntry.bind("<<ComboboxSelected>>", auto_account_num)


        self.btn_save = Button(self.root, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.insert_inventory)
        self.btn_save.place(x=10, y=270)

        # this is for search frame

        self.trans_dateFrom_entry  = DateEntry(self.root, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
        self.trans_dateFrom_entry.place(x=380, y=5)
        self.trans_dateFrom_entry.configure(justify='center')

        self.trans_date_lbl = Label(self.root, text='TO', width=5, height=1, bg='yellow', fg='black',
                               font=('Arial', 9), anchor='center')
        self.trans_date_lbl .place(x=510, y=5)

        self.trans_dateTo_entry  = DateEntry(self.root, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
        self.trans_dateTo_entry.place(x=570, y=5)
        self.trans_dateTo_entry.configure(justify='center')

        self.categoryEntry_search = ttk.Combobox(self.root, width=20,font=('Arial', 10))
        self.categoryEntry_search['values'] =self.inve_category()
        self.categoryEntry_search.place(x=700, y=5)

        self.btn_display = Button(self.root, text='Display', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.display_inventory)
        self.btn_display.place(x=975, y=5)


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
                                                'Unit','Amount','Running Balance'),
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
        self.inventoryTreeview.heading('Running Balance', text="Running Balance", anchor=CENTER)
         


        self.inventoryTreeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
        self.inventoryTreeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='center')
        self.inventoryTreeview.column('#2', stretch=NO, minwidth=0, width=70, anchor='sw')
        self.inventoryTreeview.column('#3', stretch=NO, minwidth=0, width=150, anchor='sw')
        self.inventoryTreeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
        self.inventoryTreeview.column('#5', stretch=NO, minwidth=0, width=70, anchor='e')
        self.inventoryTreeview.column('#6', stretch=NO, minwidth=0, width=100, anchor='e')
        self.inventoryTreeview.column('#7', stretch=NO, minwidth=0, width=115, anchor='e')
        
       
    
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

        if self.categoryEntry_search.get():

            myresult = Database.select_all_from_inventoryData_withCategory(self.categoryEntry_search.get())
            self.Totalstockamount_view = 0
            for i in myresult:
                self.productID_view = i[1]   
                self.brand_view = i[2]   
                self.description_view = i[3]  
                self.quantity_view = i[4] 
                self.unit_view = i[6]
                self.stockamount_view2 = i[7]
                self.Totalstockamount_view+= self.stockamount_view2
                self.Totalstockamount_view2 ='{:,.2f}'.format(self.Totalstockamount_view)
                self.stockamount_view ='{:,.2f}'.format(i[7])

                self.inventoryTreeview.insert('', 'end', values=(self.productID_view,self.brand_view,
                                    self.description_view,self.quantity_view,self.unit_view,self.stockamount_view,
                                    self.Totalstockamount_view2))
        else:
            myresult = Database.select_all_from_inventoryData()
            self.Totalstockamount_view = 0
            for i in myresult:
                self.productID_view = i[1]   
                self.brand_view = i[2]   
                self.description_view = i[3]  
                self.quantity_view = i[4] 
                self.unit_view = i[6]
                self.stockamount_view2 = i[7]
                self.Totalstockamount_view+= self.stockamount_view2
                self.Totalstockamount_view2 ='{:,.2f}'.format(self.Totalstockamount_view)
                self.stockamount_view ='{:,.2f}'.format(i[7])

                self.inventoryTreeview.insert('', 'end', values=(self.productID_view,self.brand_view,
                                    self.description_view,self.quantity_view,self.unit_view,self.stockamount_view,
                                    self.Totalstockamount_view2))
    def inve_category(self):
        """This function is for Displaying inventory category"""
        # from inventory_database import Database
        # Database.initialize()
        # agg_result = Database.select_all_category_from_category()
        mydb._open_connection()
        
        cursor.execute('SELECT category FROM category ORDER by category ASC')

        agg_result = cursor.fetchall()

        data = []
        for x in agg_result:
            data.append(x[0])
        
        return data
        

    def start_main_loop(self):

        self.root.mainloop()


c = Controller(Inventory())
c.start()

