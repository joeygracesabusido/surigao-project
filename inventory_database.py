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

        Database.DATABASE._open_connection()
        try: 
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS inventory_onhand (id INT AUTO_INCREMENT PRIMARY KEY, 
                            product_id VARCHAR(100), 
                            brand VARCHAR(100),
                            description VARCHAR(250),
                            quantity DECIMAL(9,2),
                            price DECIMAL(9,2),
                            stockValue DECIMAL(9,2) GENERATED ALWAYS AS (quantity*price) STORED,
                            category VARCHAR(300),
                            date_credited date,
                            time_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            INDEX (category),
                            CONSTRAINT FK_category FOREIGN KEY (category)
                            REFERENCES category(category) ON UPDATE CASCADE ON DELETE CASCADE,
                             UNIQUE (product_id))ENGINE = InnoDB;
                                        """)
                    
            
                            
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")

        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()


    @staticmethod
    def insert_inventoryOnhand(product_id,brand,description,
                                quantity,price,date,category):
        """This is to insert to database Inventory and inventory_onhand Table"""
        Database.DATABASE._open_connection() # to open database connection

        try:
           
            data = ( "INSERT INTO inventory_onhand (product_id,brand,\
                                description,quantity,price,date_credited,category)"
                    "VALUES(%s,%s,%s,%s,%s,%s,%s)")
            val = (product_id,brand,description,quantity,
                            price,date,category)
            #                  
            # cursor.execute(data)              
            cursor.execute(data,val) 
           
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:

            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def select_Inventory(id):
        """
        This function is for querying with parameters of ID
        """
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM inventory_onhand \
                WHERE product_id = "'+id+'"')

            cursor.execute(data)
            return cursor.fetchone()
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def select_all_category_from_category():
        """
        This function is for querying with parameters of ID
        """
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT category FROM category')

            cursor.execute(data)
            return cursor.fetchall()
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()