from tkinter import *

class Controller:
    def __init__(self,view):
        self.view = view
    def start(self):
        self.view.set_up(self)

class Inventory():
    """This is for Inventory View"""

    def set_up(self):

        self.root = Tk()
        self.root.title("JRS SYSTEM")
        self.root.geometry("450x450")
        
        self.root.config(bg="black")
        

        self.productID = Label(self.root, text='Equipment ID:', width=15, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
        self.productID.place(x=10, y=30)

        global euipment_id
        self.euipment_id = Entry(self.root, width=15, font=('Arial', 12))
        self.euipment_id.place(x=150, y=30)

   
        self.root.mainloop()


c = Controller(Inventory)
c.start()

