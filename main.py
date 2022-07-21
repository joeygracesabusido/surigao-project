import mysql.connector
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

mydb = mysql.connector.connect(
            host="192.46.225.247",
            user="joeysabusido",
            password="Genesis@11",
            database="ldsurigao",
            auth_plugin='mysql_native_password')
cursor = mydb.cursor()



# this is to create table for admin login
try: 
    cursor.execute(
            "CREATE TABLE IF NOT EXISTS admin_login (id INT AUTO_INCREMENT PRIMARY KEY,fullname VARCHAR(100),\
                username VARCHAR(100), password_admin VARCHAR(100), admin_status VARCHAR(100))")
except Exception as ex:
    print("Error", f"Error due to :{str(ex)}")

try: 
    cursor.execute(
            "CREATE TABLE IF NOT EXISTS employee_login (id INT AUTO_INCREMENT PRIMARY KEY,fullname VARCHAR(100),\
                username VARCHAR(100), password_employee VARCHAR(100), employee_status VARCHAR(100))")
except Exception as ex:
    print("Error", f"Error due to :{str(ex)}")

 
# try: 
#     cursor.execute(
#         """CREATE TABLE IF NOT EXISTS inventory_onhand (id INT AUTO_INCREMENT PRIMARY KEY, 
#                     product_id VARCHAR(100), 
#                     brand VARCHAR(100),
#                     description VARCHAR(250),
#                     quantity DECIMAL(9,2),
#                     price DECIMAL(9,2),
#                     stockValue DECIMAL(9,2) GENERATED ALWAYS AS (quantity*price) STORED,
#                     date_credited date,
#                     time_update TIMESTAMP,
#                     UNIQUE (product_id))
#                                 """)
            
# except Exception as ex:
#     print("Error", f"Error due to :{str(ex)}")





# this is to insert admin log in 

# try:
#     cursor.execute("INSERT INTO  admin_login (username, password_admin,admin_status) \
#                         VALUES('joeysabusido', 'genesis@11','approved')")
# except Exception as ex:
#     print("Error", f"Error due to :{str(ex)}")

mydb.commit()

# cursor.execute('SELECT * FROM admin_login')
# for x in cursor:
#     print(x)

root = Tk()
root.title("JRS SYSTEM")

width = 750
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="cyan")

#load = Image.open("image\login.png").convert("RGB")
load = PIL.Image.open("image\login.png")
load =load.resize((150, 125), PIL.Image.ANTIALIAS)
logo_icon = ImageTk.PhotoImage(load)
#==============================================Clear Midform======================================================
def clearFrame():
    # destroy all widgets from frame
    for widget in MidViewForm9.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    MidViewForm9.pack_forget()
#==============================================Inventory Frame ====================================================
def inve_category():
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
class View(ABC):
    def setup(self,controller):
        pass
    def clear_inputs(self):
        pass
    def search_inventory(self):
        pass
    def insertPurchases(self):
        pass
    def inventory_treeview_display(self):
        pass
    def inventory_treevie_list(self):
        pass

class insert_inventoryController():
    def __init__(self,view:View):
        self.view = view

    def start(self):# this is to start up Invenotry View
        clearFrame()
        self.view.set_up(self)
        # self.view.inve_category()
        self.view.inventory_treevie_list()

    def click_inventorySearch(self):
        # self.view.clear_inputs()
        self.view.search_inventory()
    def clcik_save_inventoryBtn(self):
        self.view.insertPurchases()

class Insert_purchasesView(View):
    """This is for insert Inventory View"""
    def set_up(self,controller):

        # self.insert_inventoryFrame = Toplevel()
        # self.insert_inventoryFrame.title("Inventory Insert")
        # self.width = 1250
        # height = 450
        # screen_width = self.insert_inventoryFrame.winfo_screenwidth()
        # screen_height = self.insert_inventoryFrame.winfo_screenheight()
        # x = (screen_width / 2) - (width / 2)
        # y = (screen_height / 2) - (height / 2)
        # self.insert_inventoryFrame.geometry("%dx%d+%d+%d" % (width, height, x, y))
        # self.insert_inventoryFrame.resizable = True
        # self.insert_inventoryFrame.config(bg="black")
        
        self.insert_inventoryFrame = Frame(MidViewForm9, width=1250, height=550, bd=2, bg='gray', relief=SOLID)
        self.insert_inventoryFrame.place(x=20, y=8)


        self.trans_date_lbl = Label(self.insert_inventoryFrame, text='Date', width=15, height=1, bg='yellow', fg='black',
                               font=('Arial', 10), anchor='e')
        self.trans_date_lbl .place(x=10, y=15)

        
        self.trans_date_entry  = DateEntry(self.insert_inventoryFrame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
        self.trans_date_entry.place(x=150, y=15)
        self.trans_date_entry.configure(justify='center')

        self.mris_lbl = Label(self.insert_inventoryFrame, text='MRIS no.:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.mris_lbl.place(x=10, y=45)

    
        self.mris_entry = Entry(self.insert_inventoryFrame, width=15, font=('Arial', 10))
        self.mris_entry.place(x=150, y=45)

        self.invoice_lbl = Label(self.insert_inventoryFrame, text='Invoice no.:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.invoice_lbl.place(x=10, y=75)

    
        self.invoice_entry = Entry(self.insert_inventoryFrame, width=15, font=('Arial', 10))
        self.invoice_entry.place(x=150, y=75)



        self.productID = Label(self.insert_inventoryFrame, text='Product ID:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.productID.place(x=10, y=105)

    
        self.product_id_entry = Entry(self.insert_inventoryFrame, width=15, font=('Arial', 10))
        self.product_id_entry.place(x=150, y=105)

        self.brand_lbl = Label(self.insert_inventoryFrame, text='Brand:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.brand_lbl.place(x=10, y=135)

    
        self.brand_inv = Entry(self.insert_inventoryFrame, width=15, font=('Arial', 10))
        self.brand_inv.place(x=150, y=135)

        

        self.description_lbl = Label(self.insert_inventoryFrame, text='Description:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.description_lbl.place(x=10, y=165)

        self.descrtip_inv_entry = scrolledtext.ScrolledText(self.insert_inventoryFrame,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
        self.descrtip_inv_entry.place(x=150, y=165)

        self.quanity_lbl = Label(self.insert_inventoryFrame, text='Quantity:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.quanity_lbl.place(x=10, y=225)

        self.quantity_inv = Entry(self.insert_inventoryFrame, width=15, font=('Arial', 10))
        self.quantity_inv.place(x=150, y=225)

        self.price_lbl = Label(self.insert_inventoryFrame, text='Price:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.price_lbl.place(x=10, y=255)

        self.price_inv = Entry(self.insert_inventoryFrame, width=15, font=('Arial', 10))
        self.price_inv.place(x=150, y=255)

        self.unit_lbl = Label(self.insert_inventoryFrame, text='Unit:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.unit_lbl.place(x=10, y=285)

        self.unit_inv = Entry(self.insert_inventoryFrame, width=15, font=('Arial', 10))
        self.unit_inv.place(x=150, y=285)

        self.category_lbl = Label(self.insert_inventoryFrame, text='Category:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.category_lbl.place(x=10, y=315)

        self.categoryEntry = ttk.Combobox(self.insert_inventoryFrame, width=20,font=('Arial', 10))
        self.categoryEntry['values'] = inve_category()
        self.categoryEntry.place(x=150, y=315)


        self.btn_search = Button(self.insert_inventoryFrame, text='Search', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.click_inventorySearch)
        self.btn_search.place(x=270, y=105)

        self.btn_save_purchase = Button(self.insert_inventoryFrame, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.clcik_save_inventoryBtn)
        self.btn_save_purchase.place(x=10, y=350)

        self.inventoryTreeview_form = Frame(self.insert_inventoryFrame, width=700, height=10)
        self.inventoryTreeview_form.place(x=370, y=40)

        # this is for search fields

        


        # This is for Tree view frame for Insert Purchases
        style = ttk.Style(self.insert_inventoryFrame)
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=20,
                        fieldbackground="white")
    
        
        
        
        scrollbarx = Scrollbar(self.inventoryTreeview_form, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.inventoryTreeview_form, orient=VERTICAL)
        
        self.inventoryTreeview = ttk.Treeview(self.inventoryTreeview_form,
                                                columns=('Date','Product ID','Brand',
                                                 'Description','Quantity','Price','Amount'),
                                                selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                                xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.inventoryTreeview.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.inventoryTreeview.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.inventoryTreeview.heading('Date', text="Date", anchor=CENTER)
        self.inventoryTreeview.heading('Product ID', text="Product ID", anchor=CENTER)
        self.inventoryTreeview.heading('Brand', text="Brand", anchor=CENTER)
        self.inventoryTreeview.heading('Description', text="Descrtiption", anchor=CENTER)
        self.inventoryTreeview.heading('Quantity', text="Quantity", anchor=CENTER)
        self.inventoryTreeview.heading('Price', text="Price", anchor=CENTER)
        self.inventoryTreeview.heading('Amount', text="Amount", anchor=CENTER)
        


        self.inventoryTreeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
        self.inventoryTreeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='center')
        self.inventoryTreeview.column('#2', stretch=NO, minwidth=0, width=80, anchor='sw')
        self.inventoryTreeview.column('#3', stretch=NO, minwidth=0, width=120, anchor='sw')
        self.inventoryTreeview.column('#4', stretch=NO, minwidth=0, width=200, anchor='e')
        self.inventoryTreeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
        self.inventoryTreeview.column('#6', stretch=NO, minwidth=0, width=100, anchor='e')
        self.inventoryTreeview.column('#7', stretch=NO, minwidth=0, width=100, anchor='e')
        
       
    
        self.inventoryTreeview.pack()
    
    def clear_inputs(self):
        """This is to clear input fields"""
        self.product_id_entry.delete(0, END)
        self.brand_inv.delete(0, END)
        self.descrtip_inv_entry.delete('1.0', END)
        self.price_inv.delete(0, END)
        self.unit_inv.delete(0, END)


    def search_inventory(self):
        """This is to search invenotry using product ID"""
        from inventory_database import Database
        Database.initialize()

        self.productId_search = self.product_id_entry.get()
        myresult = Database.select_One_from_inventoryData(product_id=self.product_id_entry.get())

        for i in myresult:
            self.productIdSearch = i[1]
            self.brandSearch = i[2]
            self.descriptionSearch = i[3]
            self.priceSearch = i[5]
            self.unit_invSearch = i[6]
            self.categorySearch = i[8]
            

            self.product_id_entry.delete(0, END)
            self.product_id_entry.insert(0, (self.productIdSearch))

            self.brand_inv.delete(0, END)
            self.brand_inv.insert(0, (self.brandSearch))

            self.descrtip_inv_entry.delete('1.0', END)
            self.descrtip_inv_entry.insert('1.0',(self.descriptionSearch))

            self.unit_inv.delete(0, END)
            self.unit_inv.insert(0, (self.unit_invSearch))

            self.categoryEntry.delete(0, END)
            self.categoryEntry.insert(0,(self.categorySearch))


            self.price_inv.delete(0, END)
            self.price_inv.insert(0,(self.priceSearch))

    def insertPurchases(self):
        """This function is for inserting data to purchases Table using Front End"""
        
        from inventory_database import Database
        Database.initialize()
        today = date.today()
        dateTime = datetime.now()
        transDate_insert = self.trans_date_entry.get()
        mris_no_insert = self.mris_entry.get()
        invoice_no_insert = self.mris_entry.get()
        productID_Insert = self.product_id_entry.get()
        brand_inv_Insert = self.brand_inv.get()
        description_insert = self.descrtip_inv_entry.get('1.0', 'end-1c')
        quantity_insert = self.quantity_inv.get()
        price_insert = self.price_inv.get()
        categoryInsert = self.categoryEntry.get()
        unitInsert = self.unit_inv.get()
        date_insert = today

        myresult = Database.select_One_from_inventoryData(productID_Insert)
        totalQuantity_update = 0
        for i in myresult:
            quantitySearch = i[4]
            totalQuantity_update = float(quantity_insert) + float(quantitySearch)
            totalQuantity_update2 = str(totalQuantity_update)
        if mris_no_insert =='' or invoice_no_insert=='' or productID_Insert =='' or brand_inv_Insert ==''\
                        or description_insert=='' or quantity_insert=='' or price_insert==''\
                            or categoryInsert =='' or unitInsert =='':
            messagebox.showinfo('Please fill up  blank entry field/s ')
        else:
            Database.insert_purchases(transDate=transDate_insert, mris_no=mris_no_insert,invoice_no=invoice_no_insert,
                                    product_id=productID_Insert,brand=brand_inv_Insert,
                                    description=description_insert,quantity=quantity_insert,
                                    price=price_insert,date=date_insert,category=categoryInsert,unit=unitInsert)
            messagebox.showinfo('Your data has been Save')

            try:
                Database.update_inventory_onhand(productID_Insert,totalQuantity_update2,dateTime)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to :{str(ex)}")

    def inventory_treeview_display(self):
        self.inventoryTreeview.delete(*self.inventoryTreeview.get_children())
        return self.inventory_treevie_list()

    def inventory_treevie_list(self):
        """This function is for querying for treeview for inventory Database"""
        from inventory_database import Database
        Database.initialize()   

        myresult = Database.select_all_from_purchase()

        for i in myresult:
            self.transDate_view = i[1]
            self.productID_view = i[4]   
            self.brand_view = i[5]   
            self.description_view = i[6]  
            self.quantity_view = i[7] 
            self.price_view =  '{:,.2f}'.format(i[8])
            self.stockamount_view = '{:,.2f}'.format(i[9])
            
           

            self.inventoryTreeview.insert('', 'end', values=(self.transDate_view,
                                    self.productID_view,self.brand_view,
                                self.description_view,self.quantity_view,
                                self.price_view, self.stockamount_view))

    

class inventoryController():
    def __init__(self,view):
        self.view = view

    def start(self):# this is to start up Invenotry View
        clearFrame()
        self.view.set_up(self) 
        self.view.inventory_treeview_display()


    def handle_clear_entry_inventory(self):
        self.view.clear_list()

    def insert_inventory(self):
        self.view.insert_inventoryOnhand()
        self.view.inventory_treeview_display()
        self.view.clear_list()
    def display_inventory(self):
        self.view.inventory_treeview_display()

class InventoryView():
    """This is for Inventory View"""

    def set_up(self,controller):

        # self.inventoryFrame = Toplevel()
        # self.inventoryFrame.title("Inventory Insert")
        # self.width = 450
        # height = 450
        # screen_width = self.inventoryFrame.winfo_screenwidth()
        # screen_height = self.inventoryFrame.winfo_screenheight()
        # x = (screen_width / 2) - (width / 2)
        # y = (screen_height / 2) - (height / 2)
        # self.inventoryFrame.geometry("%dx%d+%d+%d" % (width, height, x, y))
        # self.inventoryFrame.resizable = True
        # self.inventoryFrame.config(bg="black")


        self.inventoryFrame = Frame(MidViewForm9, width=1100, height=500, bd=2, bg='gray', relief=SOLID)
        self.inventoryFrame.place(x=170, y=8)

        self.productID = Label(self.inventoryFrame, text='Product ID:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.productID.place(x=10, y=30)

    
        self.product_id_entry = Entry(self.inventoryFrame, width=15, font=('Arial', 10))
        self.product_id_entry.place(x=150, y=30)

        self.brand_lbl = Label(self.inventoryFrame, text='Brand:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.brand_lbl.place(x=10, y=60)

    
        self.brand_inv = Entry(self.inventoryFrame, width=15, font=('Arial', 10))
        self.brand_inv.place(x=150, y=60)

        self.description_lbl = Label(self.inventoryFrame, text='Description:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.description_lbl.place(x=10, y=90)

        self.descrtip_inv_entry = scrolledtext.ScrolledText(self.inventoryFrame,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
        self.descrtip_inv_entry.place(x=150, y=90)

        self.quanity_lbl = Label(self.inventoryFrame, text='Quantity:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.quanity_lbl.place(x=10, y=150)

        self.quantity_inv = Entry(self.inventoryFrame, width=15, font=('Arial', 10))
        self.quantity_inv.place(x=150, y=150)

        self.price_lbl = Label(self.inventoryFrame, text='Price:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.price_lbl.place(x=10, y=180)

        self.price_inv = Entry(self.inventoryFrame, width=15, font=('Arial', 10))
        self.price_inv.place(x=150, y=180)

        self.unit_lbl = Label(self.inventoryFrame, text='Unit:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.unit_lbl.place(x=10, y=210)

        self.unit_inv = Entry(self.inventoryFrame, width=15, font=('Arial', 10))
        self.unit_inv.place(x=150, y=210)

        self.category_lbl = Label(self.inventoryFrame, text='Category:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.category_lbl.place(x=10, y=240)

        self.categoryEntry = ttk.Combobox(self.inventoryFrame, width=20,font=('Arial', 10))
        self.categoryEntry['values'] = inve_category()
        self.categoryEntry.place(x=150, y=240)
        # self.categoryEntry.bind("<<ComboboxSelected>>", auto_account_num)


        self.btn_save = Button(self.inventoryFrame, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.insert_inventory)
        self.btn_save.place(x=10, y=270)

        self.btn_display = Button(self.inventoryFrame, text='Display', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.display_inventory)
        self.btn_display.place(x=850, y=15)


        self.inventoryTreeview_form = Frame(self.inventoryFrame, width=700, height=10)
        self.inventoryTreeview_form.place(x=380, y=40)

        style = ttk.Style(self.inventoryFrame)
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
               


#==============================================Cost Analysis Frame ================================================
def update_equipment():
    """
    This function is to update Equipment
    """
    from equipment_database import Database
    Database.initialize()

    transID =TransID_euipment_entry.get()
    equipID = euipment_id.get()
    equipment_name = equipment_name_registry_entry.get()
    purchase_amount = amount_purchase_registry_entry.get()
    chases_number = chasis_number_entry.get()
    plate_number = plate_number_entry.get()
    date_purchase = datePurchase_entry.get()

    if transID == "":

        messagebox.showinfo('JRS','No Transaction ID has been Selected')

    else:
        data = Database.update_one_equipment(equipID,equipment_name,purchase_amount,
                                        chases_number,plate_number,date_purchase,transID)

        if data == []:
            messagebox.showinfo('JRS','Error')
        else:
            messagebox.showinfo('JRS','Data has been update')
def search_one_equipment():
    """
    this function is for searching equipment by using transaction ID
    """
    from equipment_database import Database
    Database.initialize()

    myresult = Database.select_one_equipment(id=TransID_euipment_entry.get())
    
    if myresult == []:
        messagebox.showinfo('JRS','Trans ID selected does not exist')
    for i in myresult:
        transID = i[0]
        equipID =i[1]
        equipName = i[2]
        purchasePrice = i[3]
        chases_number = i[4]
        plate_number = i[5]
        date_purchase = i[6]

        euipment_id.delete(0, END)
        euipment_id.insert(0, (equipID))

        equipment_name_registry_entry.delete(0, END)
        equipment_name_registry_entry.insert(0, (equipName))

        amount_purchase_registry_entry.delete(0, END)
        amount_purchase_registry_entry.insert(0, (purchasePrice))

        chasis_number_entry.delete(0, END)
        chasis_number_entry.insert(0, (chases_number))

        plate_number_entry.delete(0, END)
        plate_number_entry.insert(0, (plate_number))

        datePurchase_entry.delete(0, END)
        datePurchase_entry.insert(0, (date_purchase))
            

def equipment_listTreeview_frame():
    """This function is to display treeview withou duplication of data"""

    equipmentList_treeview.delete(*equipmentList_treeview.get_children())
    return equipment_listTreeview()

def equipment_listTreeview():
    """
    This function is for
    list of equipment Data
    """
    table = 'equipment'
    from equipment_database import Database
    Database.initialize()

    myresult = Database.select_all_equipment(table=table)
    
    cnt = 0
    for row in myresult:
        cnt+=1
        transID = row[0]
        equipmentID = row[1]
        chases_number = row[4]
        plate_number = row[5]
       
               
        equipmentList_treeview.insert('', 'end', values=(cnt,transID,equipmentID,
                                plate_number , chases_number ))

def insert_equipment():
    """
    This function is for
    inserting data to equipment table
    """
    from equipment_database import Database
    Database.initialize()
    from equipment_transaction import Equipment
    equipID = euipment_id.get()
    equipment_name = equipment_name_registry_entry.get()
    purchase_amount = amount_purchase_registry_entry.get()
    chases_number = chasis_number_entry.get()
    plate_number = plate_number_entry.get()
    date_purchase = datePurchase_entry.get()

    data = Database.selectEquipment(equipID)

    if data is not None:
        messagebox.showinfo('JRS','Equipment ID is already Taken')
    else:
        if equipID =='' or equipment_name=='' or purchase_amount=='' \
            or chases_number==''or plate_number=="" or date_purchase =="":
            messagebox.showinfo('Please fill up  blank entry field/s ')
        else:
            # data2 = Equipment(equipID,equipment_name,
            #         purchase_amount,chases_number,plate_number,
            #         date_purchase)
            # data2.equipment_insert()
            
            data2 = Equipment(equipmentID = equipID, equipment_name=equipment_name,
                        purchase_price=purchase_amount,
                        chases_number=chases_number,
                        plate_number = plate_number,
                        date_purchase=date_purchase)
            data2.equipment_insert()

            messagebox.showinfo('JRS','Data has been save')
            equipment_listTreeview_frame()




def insert_equipment_frame():
    """
    This function is for
    inserting equipment
    """

    equipment_registry_frame = Frame(MidViewForm9, width=1100, height=500, bd=2, bg='gray', relief=SOLID)
    equipment_registry_frame.place(x=170, y=8)
    
    trans_label = Label(equipment_registry_frame, text='Equipment Registration',
                        width=35, height=1, bg='pink', fg='black',
                          font=('Arial', 13), anchor='center')
    trans_label.place(x=370, y=3)

    equipmentID_label = Label(equipment_registry_frame, text='Equipment ID:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    equipmentID_label.place(x=10, y=30)

    global euipment_id
    euipment_id = Entry(equipment_registry_frame, width=15, font=('Arial', 12))
    euipment_id.place(x=150, y=30)

    equipment_name_registry_lbl = Label(equipment_registry_frame, text='Equipment:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    equipment_name_registry_lbl.place(x=10, y=55)

    global equipment_name_registry_entry
    equipment_name_registry_entry = Entry(equipment_registry_frame, width=25, font=('Arial', 10))
    equipment_name_registry_entry.place(x=150, y=55)

    add_reg_label = Label(equipment_registry_frame, text='Amount Purchase:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    add_reg_label.place(x=10, y=80)

    global amount_purchase_registry_entry
    amount_purchase_registry_entry = Entry(equipment_registry_frame, width=15, font=('Arial', 10))
    amount_purchase_registry_entry.place(x=150, y=80)

    # global add_reg_entry
    # add_reg_entry = scrolledtext.ScrolledText(members_data_frame,
    #                                                       wrap=tk.WORD,
    #                                                       width=20,
    #                                                       height=3,
    #                                                       font=("Arial",
    #                                                             10))
    # add_reg_entry.place(x=110, y=80)

   
    bdate_label = Label(equipment_registry_frame, text='Date Purchase:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    bdate_label.place(x=10, y=110)
    global datePurchase_entry
    datePurchase_entry = DateEntry(equipment_registry_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10,font=('Arial', 10))
    datePurchase_entry.place(x=150, y=110)
    datePurchase_entry.configure(justify='center')
    # bday_reg.bind("<<DateEntrySelected>>", calculate_bday)

    chasis_number_lbl = Label(equipment_registry_frame, text='Chasis No.:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    chasis_number_lbl.place(x=10, y=140)

    global chasis_number_entry
    chasis_number_entry = Entry(equipment_registry_frame, width=15, font=('Arial', 10))
    chasis_number_entry.place(x=150, y=140)


    plate_number_lbl = Label(equipment_registry_frame, text='Plate No.:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    plate_number_lbl.place(x=10, y=170)

    global plate_number_entry
    plate_number_entry = Entry(equipment_registry_frame, width=15, font=('Arial', 10))
    plate_number_entry.place(x=150, y=170)

    

    btn_save = Button(equipment_registry_frame, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=insert_equipment)
    btn_save.place(x=10, y=210)

    btn_update = Button(equipment_registry_frame, text='Update', bd=2, bg='yellow', fg='black',
                              font=('arial', 10), width=10, height=1,command=update_equipment)
    btn_update.place(x=110, y=210)

    # this portion is for Searching function  using Trans ID
    transID_lbl = Label(equipment_registry_frame, text='Trans ID:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    transID_lbl.place(x=10, y=280)

    global TransID_euipment_entry
    TransID_euipment_entry = Entry(equipment_registry_frame, width=15, font=('Arial', 10))
    TransID_euipment_entry.place(x=150, y=280)
    
    
    btn_search = Button(equipment_registry_frame, text='Search', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=10, height=1,command=search_one_equipment)
    btn_search.place(x=280, y=280)


    equipmentlist_view_Form = Frame(equipment_registry_frame, width=500, height=10)
    equipmentlist_view_Form.place(x=370, y=30)

    style = ttk.Style(equipment_registry_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="white",
                    foreground="black",
                    rowheight=15,
                    fieldbackground="yellow")
   
    
    
    global equipmentList_treeview
    scrollbarx = Scrollbar(equipmentlist_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(equipmentlist_view_Form, orient=VERTICAL)
    
    equipmentList_treeview = ttk.Treeview(equipmentlist_view_Form,
                                             columns=('Count','Trans ID','ID','PLATE NO', "CHASES NO"
                                              ),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=equipmentList_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=equipmentList_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    equipmentList_treeview.heading('Count', text="Count", anchor=CENTER)
    equipmentList_treeview.heading('Trans ID', text="Trans ID", anchor=CENTER)
    equipmentList_treeview.heading('ID', text="ID", anchor=CENTER)
    equipmentList_treeview.heading('PLATE NO', text="PLATE NO.", anchor=CENTER)
    equipmentList_treeview.heading('CHASES NO', text="CHASES NO.", anchor=CENTER)
   


    equipmentList_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    equipmentList_treeview.column('#1', stretch=NO, minwidth=0, width=100, anchor='e')
    equipmentList_treeview.column('#2', stretch=NO, minwidth=0, width=100, anchor='e')
    equipmentList_treeview.column('#3', stretch=NO, minwidth=0, width=100, anchor='e')
    equipmentList_treeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
    equipmentList_treeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
   

    equipmentList_treeview.pack()
    equipment_listTreeview_frame()
  


# ==============================================Insert Admin User ==================================================

def insert_user_registration():
    """
    This function is for inserting
    user registration
    """
    mydb._open_connection()
    cursor = mydb.cursor()

    admin_status = 'for approval'
    if userName_entry_registry.get == "" or password_entry_registration.get() == "":
            lbl_result_registration.config(text="Please complete the required field!", fg="red")
    elif password_entry_registration.get() != password_register_Reentry.get():
            lbl_result_registration.config(text="Password did not Match", fg="red")
    else:
        try:
            cursor.execute("INSERT INTO  admin_login (fullname,username, password_admin,admin_status)" \
                               " VALUES(%s, %s, %s,%s)",\
                               (full_name_registry.get(),userName_entry_registry.get(),\
                                 password_entry_registration.get(),admin_status) \
                                )
            messagebox.showinfo("JRS",'Data has been save')
            mydb.commit()
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        



# =====================================Registration =============================================
def user_regsitration_frame():
    """
    This function is for
    user registration 
    """
    global registration_frame
    registration_frame = Toplevel()
    registration_frame.title("User Regsitration")
    width = 550
    height = 400
    screen_width = registration_frame.winfo_screenwidth()
    screen_height = registration_frame.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    registration_frame.geometry("%dx%d+%d+%d" % (width, height, x, y))
    registration_frame.resizable = True
    registration_frame.config(bg="cyan")



    full_name_label = Label(registration_frame,text='Full Name',width=14,height=1,bg='yellow',fg='black',
                                font=('Arial',11),anchor='c')
    full_name_label.place(x=100,y=130)

    global full_name_registry
    full_name_registry = Entry(registration_frame, width=22, font=('Arial', 12))
    #userName_entry.insert(0, u'enter username')
    full_name_registry.place(x=250, y=130)

    username_lbl = Label(registration_frame,text='Username',width=14,height=1,bg='yellow',fg='black',
                                font=('Arial',11),anchor='c')
    username_lbl.place(x=100,y=160)

    global userName_entry_registry
    userName_entry_registry = Entry(registration_frame, width=22, font=('Arial', 12))
    #userName_entry.insert(0, u'enter username')
    userName_entry_registry.place(x=250, y=160)


    password_lbl = Label(registration_frame,text='Password',width=14,height=1,bg='yellow',fg='black',
                                font=('Arial',11),anchor='c')
    password_lbl.place(x=100,y=190)

    global password_entry_registration
    password_entry_registration = Entry(registration_frame, width=22, font=('Arial', 12),show="*")
    #password_entry.insert(0,u'enter password')
    password_entry_registration.place(x=250, y=190)


    password_lbl_retype = Label(registration_frame,text='Password Retype',width=14,height=1,bg='yellow',fg='black',
                                font=('Arial',11),anchor='c')
    password_lbl_retype.place(x=100,y=220)

    global password_register_Reentry
    password_register_Reentry = Entry(registration_frame, width=22, font=('Arial', 12),show="*")
    #password_entry.insert(0,u'enter password')
    password_register_Reentry.place(x=250, y=220)

    global lbl_result_registration
    lbl_result_registration = Label(registration_frame, text="", bg='skyblue', font=('arial', 13),anchor='c')
    lbl_result_registration.place(x=100, y=250)


    btn_login = Button(registration_frame, text="Register", font=('arial', 12), width=39,
                        command= insert_user_registration)
    btn_login.place(x=100, y=270)
   



#===============================================Log in and DashBoard Frame=============================================


def Logout():
    result = tkMessageBox.askquestion('JRS System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':

        root.deiconify()
        reportFrame.destroy()


def close():
    root.destroy()




def dashboard():
    global MidViewForm9
    global logo_icon2
    global reportFrame

    reportFrame = Toplevel()
    reportFrame.title("DashBoard")
    width = 1300
    height = 650
    screen_width = reportFrame.winfo_screenwidth()
    screen_height = reportFrame.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    reportFrame.geometry("%dx%d+%d+%d" % (width, height, x, y))
    reportFrame.resizable = False
    reportFrame.config(bg="cyan")
    
#=============================================Frame for time & others in DashBoard======================================
    TopdashboardForm = Frame(reportFrame, width=1295, height=50, bd=2, relief=SOLID)
    TopdashboardForm.place(x=1,y=8)
#============================================================= menu Bar=================================================
    c = inventoryController(InventoryView())
    insert_inventory = insert_inventoryController(Insert_purchasesView())
    # from inventoryView import Inventory,Controller # calling inventoryview.py
    # c = Controller(Inventory())

    # from insertpurchase import View2,insert_inventoryController2,Insert_purchasesView2
    # insert_inventory = insert_inventoryController2(Insert_purchasesView2())


    menubar = Menu(reportFrame)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu5 = Menu(menubar, tearoff=0)
    filemenu6 = Menu(menubar, tearoff=0)
    # filemenu7 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Logout", command = Logout)
    # filemenu.add_command(label="Exit")
    filemenu2.add_command(label="Items Registration", command=c.start)
    filemenu2.add_command(label="Add Purchases", command=insert_inventory.start)
    filemenu2.add_command(label="View")
   
    
    filemenu3.add_command(label="Daily Transactions")
    filemenu4.add_command(label="Accounting Module")
    filemenu5.add_command(label="Reports Module")

    filemenu6.add_command(label="Equipment Module", command=insert_equipment_frame)
    
    #filemenu7.add_command(label="New Payroll", command = payroll_transactions)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    menubar.add_cascade(label="Payroll Transactions", menu=filemenu3)
    menubar.add_cascade(label="Accounting Transaction", menu=filemenu4)
    menubar.add_cascade(label="Equipment", menu=filemenu6)
    menubar.add_cascade(label="Reports", menu=filemenu5)
    #menubar.add_cascade(label="New Payroll", menu=filemenu7)

    reportFrame.config(menu=menubar)


    MidViewForm9 = Frame(reportFrame, width=1295, height=600,bd=2,relief=SOLID)
    MidViewForm9.place(x=1, y=58)
    MidViewForm9.config(bg="cyan")


    # load2 = PIL.Image.open("image\search2.jpg")
    # load2 = load2.resize((125, 50), PIL.Image.ANTIALIAS)
    # logo_icon2 = ImageTk.PhotoImage(load2)

    UserName = userName_entry.get()
    user_label = Label(TopdashboardForm, text='Sign in as', width=17, height=1, bg='yellow', fg='gray',
                      font=('Arial', 11), anchor='c')
    user_label.place(x=5, y=15)


    user_Name_label = Label(TopdashboardForm, text='', width=17, height=1, bg='yellow', fg='gray',
                       font=('Arial', 11), anchor='c')
    user_Name_label.place(x=175, y=15)
    user_Name_label.config(text=UserName, fg="red")

    # :%a, %b %d %Y
    DateTime_label = Label(TopdashboardForm, text=f"{dt.datetime.now():%a, %b %d %Y %I:%M %p}",
                           fg="white", bg="black", font=("helvetica", 10))
    DateTime_label.place(x=1100, y=15)


USERNAME =StringVar()
PASSWORD = StringVar()



# ======================================LOGIN ============================================
def Login(event=None):
    from database_login import Database

    Database.initialize()

    
    if user_description.get() =="Admin":
        if USERNAME.get() == "" or PASSWORD.get() == "":
                lbl_result.config(text="Please complete the required field!", fg="red")
        else:
            # cursor.execute("SELECT * FROM admin_login WHERE username = %s AND password_admin = %s  AND admin_status = 'approved'",
            #                (USERNAME.get(), PASSWORD.get()))
            data = Database.login_credentials(USERNAME.get(),PASSWORD.get())

            # if cursor.fetchone() is not None:
            if data is not None:
               

                PASSWORD.set("")
                lbl_result.config(text="")
                root.withdraw()
                dashboard()


            else:
                lbl_result.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
    elif user_description.get() =="Employee":
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM employee_login WHERE username = %s AND password_user = %s AND user_status = 'approved'",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                
                PASSWORD.set("")
                lbl_result.config(text="")
                root.withdraw()
                dashboard()


            else:
                lbl_result.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
    elif user_description.get() == "":
        lbl_result.config(text="Please fill up sign in as in the required field!", fg="red")

# ================================================= label and entryfields ===========================================


global userName_entry
logolbl = Label(root,image= logo_icon)
logolbl.place(x=200,y=40)

loginlabe = Label(root,text='Sign in as',width=17,height=1,bg='yellow',fg='gray',
                            font=('Arial',14),anchor='c')
loginlabe.place(x=370,y=70)

global user_description
user_description = ttk.Combobox(root, width=19,font=('Arial',13))
user_description['values'] = ("Admin", "Employee")
user_description.place(x=370, y=105)

username_lbl = Label(root,text='Username',width=14,height=1,bg='yellow',fg='gray',
                            font=('Arial',11),anchor='c')
username_lbl.place(x=200,y=260)

userName_entry = Entry(root, width=22,textvariable = USERNAME, font=('Arial', 12))
#userName_entry.insert(0, u'enter username')
userName_entry.place(x=350, y=260)


password_lbl = Label(root,text='Password',width=14,height=1,bg='yellow',fg='gray',
                            font=('Arial',11),anchor='c')
password_lbl.place(x=200,y=290)

password_entry = Entry(root, width=22, textvariable = PASSWORD, font=('Arial', 12),show="*")
#password_entry.insert(0,u'enter password')
password_entry.place(x=350, y=290)

lbl_result = Label(root, text="", bg='skyblue', font=('arial', 13),anchor='c')
lbl_result.place(x=200, y=320)


btn_login = Button(root, text="Login", font=('arial', 12), width=39, command=Login)
btn_login.place(x=200, y=340)
btn_login.bind('<Return>', Login),


password_lbl = Label(root,text='If not Register, click button?',width=25,height=1,
                            font=('Arial',10),anchor='c')
password_lbl.place(x=170,y=390)

btn_registration = Button(root, text="Registration", font=('arial', 12),
                                 width=17,bg='gray',fg='yellow', command=user_regsitration_frame
                                )
btn_registration.place(x=380, y=390)



# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()

