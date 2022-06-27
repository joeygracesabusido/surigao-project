from typing import List
from database_login import Database
from dataclasses import dataclass,field

Database.initialize()
# cursor= Database.DATABASE.cursor()


class Login(object):
    
    def __init__(self,fullname,username,password_admin,admin_status):
      
        self.fullname = fullname
        self.username = username
        self.password_admin = password_admin
        self.admin_status = admin_status
    
    

    # @staticmethod
    def test_insert(self):
        """
        This function is 
        to insert data to admin login
        """
        Database.test_insert(fullname= self.fullname, username=self.username,
                        password_admin=self.password_admin,admin_status=self.admin_status)



   


        