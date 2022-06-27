from pickle import NONE
from dataclasses import dataclass
import mysql.connector

class Database(object):
    
    DATABASE = NONE

    def initialize():

        Database.DATABASE = mysql.connector.connect(
                                host="192.46.225.247",
                                user="joeysabusido",
                                password="Genesis@11",
                                database="ldsurigao",
                                auth_plugin='mysql_native_password')
        global cursor
        cursor = Database.DATABASE.cursor()

    @staticmethod
    def login_credentials(table,username,password):
        """
        This is for admin selection
        Data base
        """
        data = ('SELECT * FROM   '+table+' \
                 WHERE username = "'+username+'"   and admin_status = "approved" AND password_admin =  "'+password+'"')
                          
        cursor.execute(data)
        return cursor.fetchone()

    @staticmethod
    def login_credentials2(table):
        """
        This is for admin selection
        Data base
        """
        data = ('SELECT * FROM   '+table+' ')
                 
                          
        cursor.execute(data)
        return cursor.fetchall()
    # @staticmethod  
    # def test_insert(table,username,password,admin_status):
    #     """
    #     This function is 
    #     to insert data to admin login
    #     """
    #     data = ('SELECT * FROM   '+table+' \
    #              WHERE username = "'+username+'"   and admin_status = "'+admin_status+'" AND password_admin =  "'+password+'"')
                          
    #     cursor.execute(data)
        # Database.DATABASE.commit()   
        # 

    
    

    @staticmethod
    def test_insert(username,password_admin,admin_status):
        """
        This function is 
        to insert data to admin login
        """
        try:
            # data = ('INSERT INTO  admin_login (username ="'+username+'", \
            #                               password_admin"'+password_admin+'",\
            #                                  admin_status="'+admin_status+'")')
                    
            # data = 'INSERT INTO  admin_login (username,password_admin,admin_status) VALUES(%s, %s, %s)'
            # val = [('"'+username+'", "'+password_admin+'", "'+admin_status+'"' )]   

            data = 'INSERT INTO  admin_login (username,password_admin,admin_status) VALUES(%s, %s,%s)',\
                ('"'+username+'", "'+password_admin+'", "'+admin_status+'"' )    
            #                  
            cursor.execute(data)              
            # cursor.execute(data,val) 
            Database.DATABASE.commit()
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")