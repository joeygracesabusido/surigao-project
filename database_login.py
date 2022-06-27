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
    def login_credentials(username,password):
        """
        This is for admin selection
        Data base
        """
        data = ('SELECT * FROM admin_login   \
                 WHERE username = %s   and admin_status = "approved" AND password_admin = %s')
        val =(username,password)
                          
        cursor.execute(data,val)
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
   

    @staticmethod
    def test_insert(fullname,username,password_admin,admin_status):
        """
        This function is 
        to insert data to admin login
        """
        try:
           
            data = ( "INSERT INTO admin_login (fullname,username,password_admin,admin_status)"
                    "VALUES(%s,%s,%s,%s)")
            val = (fullname,username,password_admin,admin_status)
            #                  
            # cursor.execute(data)              
            cursor.execute(data,val) 
            Database.DATABASE.commit()
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")

    @staticmethod
    def delete_user(table,id):
        """
        This function is 
        to insert data to admin login
        """
        try:
            
            data = ('DELETE  FROM   '+table+' \
                WHERE id = "'+id+'"')       
            #                  
            # cursor.execute(data)              
            cursor.execute(data) 
            Database.DATABASE.commit()
            return ("Data has been deleted")
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")