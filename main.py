import mysql.connector
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkcalendar import DateEntry
from tkcalendar import DateEntry as TkcDateEntry
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter import messagebox

from PIL import Image, ImageTk
import PIL.Image
import datetime as dt

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

#==============================================Cost Analysis Frame ================================================
def insert_equipment():
    """
    This function is for
    inserting equipment
    """

    members_data_frame = Frame(MidViewForm9, width=400, height=500, bd=2, bg='gray', relief=SOLID)
    members_data_frame.place(x=200, y=8)
    
    trans_label = Label(members_data_frame, text='Inserting Church Member',
                        width=35, height=1, bg='pink', fg='black',
                          font=('Arial', 13), anchor='center')
    trans_label.place(x=230, y=3)

    l_name_reg_label = Label(members_data_frame, text='Last Name:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    l_name_reg_label.place(x=10, y=30)

    global last_name_member_reg
    last_name_member_reg = Entry(members_data_frame, width=15, font=('Arial', 12))
    #userName_entry.insert(0, u'enter username')
    last_name_member_reg.place(x=110, y=30)

    f_name_reg_label = Label(members_data_frame, text='First Name:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    f_name_reg_label.place(x=10, y=55)

    global first_name_member_reg
    first_name_member_reg = Entry(members_data_frame, width=15, font=('Arial', 12))
    #userName_entry.insert(0, u'enter username')
    first_name_member_reg.place(x=110, y=55)

    add_reg_label = Label(members_data_frame, text='Address:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    add_reg_label.place(x=10, y=80)

    global add_reg_entry
    add_reg_entry = scrolledtext.ScrolledText(members_data_frame,
                                                          wrap=tk.WORD,
                                                          width=20,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
    add_reg_entry.place(x=110, y=80)

   
    bdate_label = Label(members_data_frame, text='Birth Day:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    bdate_label.place(x=10, y=138)
    global bday_reg
    bday_reg = DateEntry(members_data_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10,font=('Arial', 12))
    bday_reg.place(x=110, y=138)
    bday_reg.configure(justify='center')
    # bday_reg.bind("<<DateEntrySelected>>", calculate_bday)

    age_reg_label = Label(members_data_frame, text='Age:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    age_reg_label.place(x=10, y=163)

    global age_member_reg
    age_member_reg = Entry(members_data_frame, width=15, font=('Arial', 12))
    age_member_reg.place(x=110, y=163)

    age_reg_label = Label(members_data_frame, text='Ministry:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    age_reg_label.place(x=10, y=188)

    global ministry_reg_entry
    ministry_reg_entry = ttk.Combobox(members_data_frame, width=20,font=('Arial', 12))
    ministry_reg_entry['values'] = 'Test'
    ministry_reg_entry.place(x=110, y=188)

    contact_reg_label = Label(members_data_frame, text='Contact No:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    contact_reg_label.place(x=10, y=213)

    global contact_member_reg
    contact_member_reg = Entry(members_data_frame, width=15, font=('Arial', 12))
    contact_member_reg.place(x=110, y=213)

    search_input_mReg_label = Label(members_data_frame, text='Search ID :', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    search_input_mReg_label.place(x=10, y=300)

    global search_input_mReg_entry
    search_input_mReg_entry = Entry(members_data_frame, width=15, font=('Arial', 12))
    search_input_mReg_entry.place(x=110, y=300)

    btn_search_mr = Button(members_data_frame, text='Search', bd=2, bg='yellow green', fg='black',
                              font=('arial', 10), width=10, height=1)
    btn_search_mr.place(x=240, y=300)
    
    
    btn_save = Button(members_data_frame, text='Save', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=10, height=1)
    btn_save.place(x=10, y=243)

    btn_update = Button(members_data_frame, text='Update', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1)
    btn_update.place(x=110, y=243)

    btn_delete = Button(members_data_frame, text='Delete', bd=2, bg='red', fg='white',
                              font=('arial', 10), width=10, height=1)
    btn_delete.place(x=210, y=243)


    memberslist_view_Form = Frame(members_data_frame, width=500, height=10)
    memberslist_view_Form.place(x=330, y=30)

    style = ttk.Style(members_data_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    rowheight=15,
                    fieldbackground="yellow")
   
    
    
    global membersList_treeview
    scrollbarx = Scrollbar(memberslist_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(memberslist_view_Form, orient=VERTICAL)
    
    membersList_treeview = ttk.Treeview(memberslist_view_Form,
                                             columns=('Count','ID','LNAME', "FNAME","MINISTRY",
                                              'CONTACT'),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=membersList_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=membersList_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    membersList_treeview.heading('Count', text="Count", anchor=CENTER)
    membersList_treeview.heading('ID', text="ID", anchor=CENTER)
    membersList_treeview.heading('LNAME', text="Last Name", anchor=CENTER)
    membersList_treeview.heading('FNAME', text="First Name", anchor=CENTER)
    membersList_treeview.heading('MINISTRY', text="Ministry", anchor=CENTER)
    membersList_treeview.heading('CONTACT', text="Contact No.", anchor=CENTER)


    membersList_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    membersList_treeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='e')
    membersList_treeview.column('#2', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#3', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#6', stretch=NO, minwidth=0, width=100, anchor='e')

    membersList_treeview.pack()
  


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
    menubar = Menu(reportFrame)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu5 = Menu(menubar, tearoff=0)
    filemenu6 = Menu(menubar, tearoff=0)
    #filemenu7 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Logout", command = Logout)
    # filemenu.add_command(label="Exit")
    filemenu2.add_command(label="Product Registration")
    filemenu2.add_command(label="Add new")
    filemenu2.add_command(label="View")
    filemenu3.add_command(label="Payroll")
    filemenu3.add_command(label="Clients Registration")
    filemenu3.add_command(label="Daily Transactions")
    filemenu4.add_command(label="Accounting Module")
    filemenu5.add_command(label="Reports Module")

    filemenu6.add_command(label="Equipment Module", command=insert_equipment)
    
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

