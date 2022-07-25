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
from threading import Thread

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




class Viewwithdrawal(ABC):
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
    def clear_inputs(self):
        pass

class insert_withdrawalController():
    def __init__(self,view:Viewwithdrawal):
        self.view = view

    def start(self):# this is to start up Invenotry View
        
        self.view.set_up(self)
        # self.view.inve_category()
        self.view.start_main_loop()
        # self.view.inve_category()
        # self.view.inventory_treeview_display()
        # self.inventory_treeview_display()

    def click_inventorySearch(self):
        # self.view.clear_inputs()
        self.view.search_inventory()
    def clcik_save_inventoryBtn(self):
        self.view.insertPurchases()
        self.view.inventory_treeview_display()
        # self.clear_inputs()

    def clickBtn_display(self):
        self.view.inventory_treeview_display()

class Insert_withdrawal(Viewwithdrawal):
    """This is for insert Inventory View"""
    def set_up(self,controller):
        width = 1250
        height = 600
        self.root = Tk()
        self.root.title("Parts Withdrawal")
       
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(False,False)
        self.root.config(bg="black")
        
        # self.insert_inventoryFrame = Frame(self.root, width=820, height=575, bd=2, bg='gray', relief=SOLID)
        # self.insert_inventoryFrame.place(x=420, y=30)

        
        self.trans_date_lbl = Label(self.root, text='Date', width=15, height=1, bg='yellow', fg='black',
                               font=('Arial', 10), anchor='e')
        self.trans_date_lbl .place(x=10, y=40)

        
        self.trans_date_entry  = DateEntry(self.root, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
        self.trans_date_entry.place(x=150, y=40)
        self.trans_date_entry.configure(justify='center')



        self.productID = Label(self.root, text='Product ID:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.productID.place(x=10, y=105)

    
        self.product_id_entry = Entry(self.root, width=15, font=('Arial', 10))
        self.product_id_entry.place(x=150, y=105)

        self.brand_lbl = Label(self.root, text='Brand:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.brand_lbl.place(x=10, y=135)

    
        self.brand_inv = Entry(self.root, width=15, font=('Arial', 10))
        self.brand_inv.place(x=150, y=135)

        

        self.description_lbl = Label(self.root, text='Description:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.description_lbl.place(x=10, y=165)

        self.descrtip_inv_entry = scrolledtext.ScrolledText(self.root,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
        self.descrtip_inv_entry.place(x=150, y=165)

        self.quanity_lbl = Label(self.root, text='Quantity:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.quanity_lbl.place(x=10, y=225)

        self.quantity_inv = Entry(self.root, width=15, font=('Arial', 10))
        self.quantity_inv.place(x=150, y=225)

        self.price_lbl = Label(self.root, text='Price:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.price_lbl.place(x=10, y=255)

        self.price_inv = Entry(self.root, width=15, font=('Arial', 10))
        self.price_inv.place(x=150, y=255)

        self.unit_lbl = Label(self.root, text='Unit:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.unit_lbl.place(x=10, y=285)

        self.unit_inv = Entry(self.root, width=15, font=('Arial', 10))
        self.unit_inv.place(x=150, y=285)

        self.category_lbl = Label(self.root, text='Category:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.category_lbl.place(x=10, y=315)

        self.categoryEntry = ttk.Combobox(self.root, width=20,font=('Arial', 10))
        self.categoryEntry['values'] = self.inve_category()
        self.categoryEntry.place(x=150, y=315)
        
        
        self.request_lbl = Label(self.root, text='Withdral Form No.:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.request_lbl.place(x=10, y=345)

    
        self.widthrawal_entry = Entry(self.root, width=15, font=('Arial', 10))
        self.widthrawal_entry.place(x=150, y=345)

        self.requestedBy_lbl = Label(self.root, text='Requested By:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.requestedBy_lbl.place(x=10, y=375)
        self.requestedBy_entry = Entry(self.root, width=25, font=('Arial', 10))
        self.requestedBy_entry.place(x=150, y=375)


        self.equipment_lbl = Label(self.root, text='Equipment:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.equipment_lbl.place(x=10, y=405)

        self.equipment_entry = ttk.Combobox(self.root, width=20,font=('Arial', 10))
        self.equipment_entry['values'] = self.equipment_list()
        self.equipment_entry.place(x=150, y=405)


        self.btn_search = Button(self.root, text='Search', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.click_inventorySearch)
        self.btn_search.place(x=270, y=105)

        self.btn_save_purchase = Button(self.root, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.clcik_save_inventoryBtn)
        self.btn_save_purchase.place(x=10, y=475)

    # this is for searching frame 

        self.dateFrom  = DateEntry(self.root, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
        self.dateFrom.place(x=370, y=5)
        self.dateFrom.configure(justify='center')

        self.to_lbl = Label(self.root, text='To:', width=7, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.to_lbl.place(x=500, y=5)

        self.dateTo  = DateEntry(self.root, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
        self.dateTo.place(x=575, y=5)
        self.dateTo.configure(justify='center')


        self.equipment_entry_search = ttk.Combobox(self.root, width=20,font=('Arial', 10))
        self.equipment_entry_search['values'] = self.equipment_list()
        self.equipment_entry_search.place(x=725, y=5)

        self.btn_display = Button(self.root, text='Display', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.clickBtn_display)
        self.btn_display.place(x=950, y=5)

        # self.thread = Thread(target=self.inventory_treevie_list)
        # self.thread.start()

        self.inventoryTreeview_form = Frame(self.root, width=700, height=20)
        self.inventoryTreeview_form.place(x=370, y=40)

        # this is for search fields

        


        # This is for Tree view frame for Insert Purchases
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
                                                columns=('Date','Product ID','Brand',
                                                 'Description','Quantity','Price','Amount','Balance',
                                                 'Equipment'),
                                                selectmode="extended", height=25, yscrollcommand=scrollbary.set,
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
        self.inventoryTreeview.heading('Balance', text="Balance", anchor=CENTER)
        self.inventoryTreeview.heading('Equipment', text="Equipment", anchor=CENTER)
        


        self.inventoryTreeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
        self.inventoryTreeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='center')
        self.inventoryTreeview.column('#2', stretch=NO, minwidth=0, width=80, anchor='sw')
        self.inventoryTreeview.column('#3', stretch=NO, minwidth=0, width=125, anchor='sw')
        self.inventoryTreeview.column('#4', stretch=NO, minwidth=0, width=125, anchor='e')
        self.inventoryTreeview.column('#5', stretch=NO, minwidth=0, width=75, anchor='e')
        self.inventoryTreeview.column('#6', stretch=NO, minwidth=0, width=75, anchor='e')
        self.inventoryTreeview.column('#7', stretch=NO, minwidth=0, width=100, anchor='e')
        self.inventoryTreeview.column('#8', stretch=NO, minwidth=0, width=100, anchor='e')
        self.inventoryTreeview.column('#9', stretch=NO, minwidth=0, width=90, anchor='e')
        
       
    
        self.inventoryTreeview.pack()
    
    def clear_inputs(self):
        """This is to clear input fields"""
       
       
        self.quantity_inv.delete(0, END)
        

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
        withdral_slpt = self.widthrawal_entry.get()
        requestedBy = self.requestedBy_entry.get()
        productID_Insert = self.product_id_entry.get()
        brand_inv_Insert = self.brand_inv.get()
        description_insert = self.descrtip_inv_entry.get('1.0', 'end-1c')
        quantity_insert = self.quantity_inv.get()
        price_insert = self.price_inv.get()
        categoryInsert = self.categoryEntry.get()
        unitInsert = self.unit_inv.get()
        equipmentInsert = self. equipment_entry.get()
        date_insert = today

        myresult = Database.select_One_from_inventoryData(productID_Insert)
        totalQuantity_update = 0
        for i in myresult:
            quantitySearch = i[4]
            totalQuantity_update = float(quantitySearch) - float(quantity_insert) 
            totalQuantity_update2 = str(totalQuantity_update)
        if withdral_slpt =='' or requestedBy=='' or productID_Insert =='' or brand_inv_Insert ==''\
                        or description_insert=='' or quantity_insert=='' or price_insert==''\
                            or categoryInsert =='' or unitInsert =='' or equipmentInsert=='':
            messagebox.showinfo('Please fill up  blank entry field/s ')
        else:
            Database.insert_withdrawal_inve(transDate=transDate_insert,product_id=productID_Insert,
                                    brand=brand_inv_Insert,description=description_insert,
                                    quantity=quantity_insert,price=price_insert,
                                    date=date_insert,category=categoryInsert,unit=unitInsert,
                                    widthrawal_slpt=withdral_slpt,requestedBy=requestedBy,
                                    equipment=equipmentInsert )
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

        if  self.equipment_entry_search.get() =='' :

            myresult = Database.select_all_withdrawal(dateFrom=self.dateFrom.get(),dateTo=self.dateTo.get())

            self.Totalstockamount_view = 0
            for i in myresult:
                self.transDate_view = i[1]
                self.productID_view = i[2]   
                self.brand_view = i[3]   
                self.description_view = i[4]  
                self.quantity_view = i[5] 
                self.price_view =  '{:,.2f}'.format(i[6])
                self.Totalstockamount_view2 = i[7]
                self.Totalstockamount_view+=self.Totalstockamount_view2
                self.Totalstockamount_view3 = '{:,.2f}'.format(self.Totalstockamount_view)
                self.stockamount_view = '{:,.2f}'.format(i[7])
                self.equiptment_view = i[11]
                
            

                self.inventoryTreeview.insert('', 'end', values=(self.transDate_view,
                                        self.productID_view,self.brand_view,
                                    self.description_view,self.quantity_view,
                                    self.price_view, self.stockamount_view,
                                    self.Totalstockamount_view3,self.equiptment_view))

        elif self.equipment_entry_search.get()!='' and self.dateFrom.get() !='' and self.dateTo.get() !='':

            myresult = Database.select_with_parameters_Date_equipment(equipment=self.equipment_entry_search.get(),
                                                        datefrom=self.dateFrom.get(),dateto=self.dateTo.get())

            self.Totalstockamount_view = 0
            for i in myresult:
                self.transDate_view = i[1]
                self.productID_view = i[2]   
                self.brand_view = i[3]   
                self.description_view = i[4]  
                self.quantity_view = i[5] 
                self.price_view =  '{:,.2f}'.format(i[6])
                self.Totalstockamount_view2 = i[7]
                self.Totalstockamount_view+=self.Totalstockamount_view2
                self.Totalstockamount_view3 = '{:,.2f}'.format(self.Totalstockamount_view)
                self.stockamount_view = '{:,.2f}'.format(i[7])
                self.equiptment_view = i[11]
              
                
            

                self.inventoryTreeview.insert('', 'end', values=(self.transDate_view,
                                        self.productID_view,self.brand_view,
                                    self.description_view,self.quantity_view,
                                    self.price_view, self.stockamount_view,
                                    self.Totalstockamount_view3,self.equiptment_view))

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

    def equipment_list(self):
        """This function is for Displaying inventory category"""
        # from inventory_database import Database
        # Database.initialize()
        # agg_result = Database.select_all_category_from_category()
        mydb._open_connection()
        
        cursor.execute('SELECT equipment_id FROM equipment ORDER by equipment_id ASC')

        agg_result = cursor.fetchall()

        data = []
        for x in agg_result:
            data.append(x[0])
        
        return data

    def start_main_loop(self):
    
        self.root.mainloop()

# c = insert_withdrawalController(Insert_withdrawal())
# c.start()