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




class ViewEquipmentStatus(ABC):
    def setup(self,controller):
        pass
    def clear_inputs(self):
        pass
    def clcik_save_Btn(self):
        pass
    def click_save_Btn(self):
        pass
    def clickBtn_display(self):
        pass
    def clickBtn_Search(self):
        pass
    def clickBtn_update(self):
        pass
   

class EquipmentStatusController():
    def __init__(self,view:ViewEquipmentStatus):
        self.view = view

    def start(self):# this is to start up Invenotry View
        
        self.view.set_up(self)
        # self.view.inve_category()
        self.view.start_main_loop()
        # self.view.inve_category()
        # self.view.inventory_treeview_display()
        # self.inventory_treeview_display()

    
    def click_save_Btn(self):
        self.view.insertdata()
        
        # self.clear_inputs()

    def clickBtn_display(self):
        self.view.mytreeView_display()

    def clickBtn_clear(self):
        self.view.clear_inputs()

    def clickBtn_Search(self):
        self.view.search_record()

    def clickBtn_update(self):
        self.view.update_record()

    def clickBtn_delete(self):
        self.view.delete_record()

class EquipmentStatus(ViewEquipmentStatus):
    """This is for insert Inventory View"""
    def set_up(self,controller):
        width = 1250
        height = 600
        self.root = Tk()
        self.root.title("Equipment Status")
       
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

        self.equipment_entry_lbl = Label(self.root, text='Equipment', width=15, height=1, bg='yellow', fg='black',
                               font=('Arial', 10), anchor='e')
        self.equipment_entry_lbl .place(x=10, y=70)

        self.equipment_entry_search = ttk.Combobox(self.root, width=20,font=('Arial', 10))
        self.equipment_entry_search['values'] = self.equipment_list()
        self.equipment_entry_search.place(x=150, y=70)
       

        self.status_lbl = Label(self.root, text='Status:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.status_lbl.place(x=10, y=105)

        self.status_entry = ttk.Combobox(self.root, width=20,font=('Arial', 10))
        self.status_entry['values'] = ('Operational', 'Breakdown')
        self.status_entry.place(x=150, y=105) 

        

        self.update_lbl = Label(self.root, text='Work Update', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.update_lbl.place(x=10, y=135)

        self.work_update_entry = scrolledtext.ScrolledText(self.root,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
        self.work_update_entry.place(x=150, y=135)

      


        

        self.btn_save_purchase = Button(self.root, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.click_save_Btn)
        self.btn_save_purchase.place(x=10, y=200)

        self.btn_update = Button(self.root, text='Update', bd=2, bg='gray', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.clickBtn_update)
        self.btn_update.place(x=110, y=200)

        # self.btn_delete = Button(self.root, text='Delete', bd=2, bg='red', fg='white',
        #                       font=('arial', 10), width=10, height=1,command=controller.clickBtn_delete)
        # self.btn_delete.place(x=210, y=475)

    # this is for searching frame 

        # self.dateFrom  = DateEntry(self.root, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
        #                             foreground='white', borderwidth=2, padx=10, pady=10)
        # self.dateFrom.place(x=370, y=5)
        # self.dateFrom.configure(justify='center')

        # self.to_lbl = Label(self.root, text='To:', width=7, height=1, bg='yellow', fg='black',
        #                   font=('Arial', 10), anchor='e')
        # self.to_lbl.place(x=500, y=5)

        # self.dateTo  = DateEntry(self.root, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
        #                             foreground='white', borderwidth=2, padx=10, pady=10)
        # self.dateTo.place(x=575, y=5)
        # self.dateTo.configure(justify='center')

        self.to_lbl = Label(self.root, text='Equipment Status:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.to_lbl.place(x=600, y=7)

        self.status_entry_search = ttk.Combobox(self.root, width=25,font=('Arial', 10))
        self.status_entry_search['values'] = ('Operational', 'Breakdown')
        self.status_entry_search.place(x=750, y=7)
        

        self.btn_display = Button(self.root, text='Display', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.clickBtn_display)
        self.btn_display.place(x=950, y=7)

      

        

        # this is for search fields

        self.searchID_entry = Entry(self.root, width=15, font=('Arial', 10))
        self.searchID_entry.place(x=10, y=435)

        self.btn_searchID = Button(self.root, text='Search ID', bd=2, bg='orange', fg='white',
                              font=('arial', 10), width=10, height=1,command=controller.clickBtn_Search)
        self.btn_searchID.place(x=130, y=435)

        


        # This is for Tree view frame for Insert Purchases

        self.myTreeView_form = Frame(self.root, width=700, height=20)
        self.myTreeView_form.place(x=370, y=50)
        
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=20,
                        fieldbackground="white")
    
        
        
        
        scrollbarx = Scrollbar(self.myTreeView_form, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.myTreeView_form, orient=VERTICAL)
        
        self.myTreeview = ttk.Treeview(self.myTreeView_form,
                                                columns=('Count','ID','Date','Equipment','Status',
                                                 'WorUpdate'),
                                                selectmode="extended", height=25, yscrollcommand=scrollbary.set,
                                                xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.myTreeview.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.myTreeview.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.myTreeview.heading('Count', text="Count", anchor=CENTER)
        self.myTreeview.heading('ID', text="ID", anchor=CENTER)
        self.myTreeview.heading('Date', text="Date", anchor=CENTER)
        self.myTreeview.heading('Equipment', text="Equipment", anchor=CENTER)
        self.myTreeview.heading('Status', text="Status", anchor=CENTER)
        self.myTreeview.heading('WorUpdate', text="Work Update", anchor=CENTER)
        
        


        self.myTreeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
        self.myTreeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='center')
        self.myTreeview.column('#2', stretch=NO, minwidth=0, width=100, anchor='sw')
        self.myTreeview.column('#3', stretch=NO, minwidth=0, width=100, anchor='sw')
        self.myTreeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
        self.myTreeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
        self.myTreeview.column('#6', stretch=NO, minwidth=0, width=350, anchor='e')
        
        
       
    
        self.myTreeview.pack()
        
    
    def clear_inputs(self):
        """This is to clear input fields"""
       
        self.trans_date_entry.delete(0, END)
        self.equipment_entry_search.delete(0, END)
        self.status_entry.delete(0, END)
        self.work_update_entry.delete('1.0', END)
        self.searchID_entry.delete(0, END)
        
        
        

    def search_record(self):
        """This is to search invenotry using product ID"""
        from equipment_database import Database
        Database.initialize()
        
        self.selected = self.myTreeview.focus()
        self.values = self.myTreeview.item(self.selected)
        self.selectedItems = self.values['values']

        
        myresult = Database.search_one_equipmentStatus(id=self.selectedItems[1])
        

        for i in myresult:
            self.idView = i[0]
            self.equipment_view = i[1]
            self.status_view = i[2] 
            self.Date_view = i[3]  
            self.workupdate_view = i[4]
         
            

            self.clear_inputs()
            self.trans_date_entry.insert(0, (self.Date_view))
            self.equipment_entry_search.insert(0, (self.equipment_view))
            self.work_update_entry.insert('1.0',(self.workupdate_view))
            self.status_entry.insert(0, (self.status_view))
            self.searchID_entry.insert(0, self.idView)

           
    def insertdata(self):
        """This function is for inserting data to purchases Table using Front End"""
        
        from equipment_database import Database
        Database.initialize()
        today = date.today()
        dateTime = datetime.now()

        transDate_insert = self.trans_date_entry.get()
        equipmentInsert = self.equipment_entry_search.get()
        statusInsert = self.status_entry.get()
        workUpdateInsert = self.work_update_entry.get('1.0', 'end-1c')

        print(transDate_insert,equipmentInsert,statusInsert,workUpdateInsert)

        date_insert = today

       
        if transDate_insert =='' or equipmentInsert=='' or statusInsert =='' or workUpdateInsert =='':
                       
            messagebox.showinfo('Please fill up  blank entry field/s ')
        else:
            Database.insert_equipmentStatus(equipment_id=equipmentInsert,status=statusInsert,
                                            date=transDate_insert,work_update=workUpdateInsert)
            messagebox.showinfo('Your data has been Save')
            self.mytreeView_display()

           

    def mytreeView_display(self):
        self.myTreeview.delete(*self.myTreeview.get_children())
        return self.mytreeView_list()

    def mytreeView_list(self):
        """This function is for querying for treeview for inventory Database"""
        from equipment_database import Database
        Database.initialize()  
      

        if self.status_entry_search.get():
            myresult = Database.select_status_equipmentStatus(status=self.status_entry_search.get())
            
            self.count = 0
            for i in myresult:
                self.count1 = 0
                self.count+=1
                self.idView = i[0]
                self.equipment_view = i[1]
                self.status_view = i[2]   
                self.workupdate_view = i[4] 
                self.date_update = i[5]  
            
            

                self.myTreeview.insert('', 'end', values=(self.count,self.idView,self.date_update,self.equipment_view,
                                        self.status_view,self.workupdate_view,))

        else:

            myresult = Database.select_all_equipmentStatus()
            self.count = 0
            for i in myresult:
                self.count1 = 0
                self.count+=1
                self.idView = i[0]
                self.equipment_view = i[1]
                self.status_view = i[2]   
                self.workupdate_view = i[4] 
                self.date_update = i[5]  
            
            

                self.myTreeview.insert('', 'end', values=(self.count,self.idView,self.date_update,self.equipment_view,
                                        self.status_view,self.workupdate_view,))
       
    def searchID(self):
        """This function is for Searching data using ID as parameter"""
        from inventory_database import Database # import class from inventory_database.py
        Database.initialize()


        self.clear_inputs()
        Idsearch = self.searchID_entry.get()
        myresult = Database.search_one_withd_ID(id=Idsearch)

        for i in myresult:

            self.idView = i[0]
            self.transDate_view = i[1]
            self.productID_view = i[2]   
            self.brand_view = i[3]   
            self.description_view = i[4]  
            self.quantity_view = i[5] 
            self.price_view =  i[6]
            self.categoryInsert = i[8]
            self.withdral_slpt = i[9]
            self.requestedBy = i[10]
            self.equiptment_view = i[11]
            self.unitInsert = i[12]

            self.trans_date_entry.insert(0,self.transDate_view)
            self.product_id_entry.insert(0,self.productID_view)
            self.brand_inv.insert(0,  self.brand_view)
            self.descrtip_inv_entry.insert('1.0', self.description_view)
            self.quantity_inv.insert(0, self.quantity_view)
            self.price_inv.insert(0, self.price_view)
            self.categoryEntry.insert(0, self.categoryInsert)
            self.unit_inv.insert(0, self.unitInsert)
            self.equipment_entry.insert(0, self.equiptment_view)
            self.widthrawal_entry.insert(0, self.withdral_slpt)
            self.requestedBy_entry.insert(0, self.requestedBy)

    def update_record(self):
        """This function is to update record for withdrawal"""
        from equipment_database import Database# import class from equipment_database.py
        Database.initialize()
        dateTime = datetime.now()

        transDate_insert = self.trans_date_entry.get()
        equipmentInsert = self.equipment_entry_search.get()
        statusInsert = self.status_entry.get()
        workUpdateInsert = self.work_update_entry.get('1.0', 'end-1c')
        searchID = self.searchID_entry.get()
        try:
            if self.searchID_entry.get():
                Database.update_equipmentStatus(equipment_id=equipmentInsert,status=statusInsert,
                                                work_update=workUpdateInsert,time_update=dateTime,id=searchID)

                messagebox.showinfo("JRS", "Data Has been save!!!")

                self.clear_inputs() 
                self.mytreeView_display()
                self.searchID_entry.delete(0, END)
            else:
                messagebox.showinfo("Error", "Please fill searcID entry field!!!")
        except Exception as ex:
                messagebox.showerror("Error", f"Error due to :{str(ex)}")

    def delete_record(self):
        """This function is to delete record"""
        from inventory_database import Database # import class from inventory_database.py
        Database.initialize()

        try:
            if self.searchID_entry.get():
                result = tkMessageBox.askquestion('JRS Software', 'Would you like to Delete record?', icon="warning")
                if result =='yes':
                    Database.delete_one_withd_ID(self.searchID_entry.get())
                    self.inventory_treeview_display()
            else:
                messagebox.showinfo("Error", "Please fill searcID entry field!!!")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")
   
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

# c = EquipmentStatusController(EquipmentStatus())
# c.start()