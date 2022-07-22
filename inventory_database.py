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
        # try: 
        #     cursor.execute(
        #         """CREATE TABLE IF NOT EXISTS inventory_onhand (id INT AUTO_INCREMENT PRIMARY KEY, 
        #                     product_id VARCHAR(100), 
        #                     brand VARCHAR(100),
        #                     description VARCHAR(250),
        #                     quantity DECIMAL(9,2),
        #                     price DECIMAL(9,2),
        #                     stockValue DECIMAL(9,2) GENERATED ALWAYS AS (quantity*price) STORED,
        #                     category VARCHAR(300),
        #                     date_credited date,
        #                     time_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        #                     INDEX (category),
        #                     CONSTRAINT FK_category FOREIGN KEY (category)
        #                     REFERENCES category(category) ON UPDATE CASCADE ON DELETE CASCADE,
        #                      UNIQUE (product_id))ENGINE = InnoDB;
        #                                 """)
                    
            
                            
        # except Exception as ex:
        #     print("Error", f"Error due to :{str(ex)}")

        # finally:
        #     Database.DATABASE.commit()
        #     Database.DATABASE.close()
        # try: 
        #     cursor.execute(
        #         """CREATE TABLE IF NOT EXISTS purchases (id INT AUTO_INCREMENT PRIMARY KEY,
        #                     transDate Date,
        #                     mris_no VARCHAR(100),
        #                     invoice_no VARCHAR(100), 
        #                     product_id VARCHAR(100), 
        #                     brand VARCHAR(100),
        #                     description VARCHAR(250),
        #                     quantity DECIMAL(9,2),
        #                     price DECIMAL(9,2),
        #                     stockValue DECIMAL(9,2) GENERATED ALWAYS AS (quantity*price) STORED,
        #                     category VARCHAR(300),
        #                     date_credited date,
        #                     time_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        #                     INDEX (category),
        #                     INDEX (product_id),
        #                     CONSTRAINT FK_categoryInsert FOREIGN KEY (category)
        #                     REFERENCES category(category) ON UPDATE CASCADE ON DELETE CASCADE,
        #                     CONSTRAINT FK_product_id FOREIGN KEY (product_id)
        #                     REFERENCES inventory_onhand(product_id) ON UPDATE CASCADE ON DELETE CASCADE
        #                     )ENGINE = InnoDB;
        #                                 """)
                    
            
                            
        # except Exception as ex:
        #     print("Error", f"Error due to :{str(ex)}")

        # finally:
        #     Database.DATABASE.commit()
        #     Database.DATABASE.close()


# this is to insert record for inventory_onhand Database
    @staticmethod
    def insert_inventoryOnhand(product_id,brand,description,
                                quantity,price,date,category,unit):
        """This is to insert to database Inventory and inventory_onhand Table"""
        Database.DATABASE._open_connection() # to open database connection

        try:
           
            data = ( "INSERT INTO inventory_onhand (product_id,brand,\
                                description,quantity,price,date_credited,category,unit)"
                    "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
            val = (product_id,brand,description,quantity,
                            price,date,category,unit)
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
            data = ('SELECT category FROM category ORDER by category ASC')

            cursor.execute(data)
            return cursor.fetchall()
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def select_all_from_inventoryData():
        """This function is for querying to inventory Database with out parameters"""
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM inventory_onhand')

            cursor.execute(data)
            return cursor.fetchall()
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def select_all_from_inventoryData_withCategory(category):
        """This function is for querying to inventory Database with out parameters"""
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM inventory_onhand where category ="'+category+'"')

            cursor.execute(data)
            return cursor.fetchall()
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def select_sum_inventoryData_withCategory(category):
        """This function is for querying to inventory Database with out parameters"""
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT category sum(quantity)as TotalQuantity, \
                            sum(stockValue) as TotalAmount\
                         FROM inventory_onhand where category ="'+category+'" \
                         GROUP by category')

            cursor.execute(data)
            return cursor.fetchall()
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def select_One_from_inventoryData(product_id):
        """This function is for queryon to invenoty Database with parameters of product inv."""
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM inventory_onhand WHERE product_id = "'+product_id+'"')

            cursor.execute(data)
            return cursor.fetchall()
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()
    @staticmethod
    def update_inventory_onhand(product_id,quantity,dateTime_update):
        """This function is for queryon to invenoty Database with parameters of product inv."""
        Database.DATABASE._open_connection()
        try:
            data = ('UPDATE inventory_onhand SET quantity = %s, time_update = %s\
                            WHERE product_id = %s')    
                   
            val = (quantity,dateTime_update,product_id)

            cursor.execute(data,val)
            # return cursor.fetchall()
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

# this is for Table purchases in the LD Surigao database
    @staticmethod
    def insert_purchases(transDate,mris_no,invoice_no,product_id,brand,description,
                                quantity,price,date,category,unit):
        """This is to insert to data to  purchases  Table"""
        Database.DATABASE._open_connection() # to open database connection

        try:
           
            data = ( "INSERT INTO purchases (transDate,mris_no,invoice_no,product_id,brand,\
                                description,quantity,price,date_credited,category,unit)"
                    "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            val = (transDate,mris_no,invoice_no,product_id,brand,description,quantity,
                            price,date,category,unit)
            #                  
            # cursor.execute(data)              
            cursor.execute(data,val) 
           
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:

            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def select_all_from_purchase():
        """This function is for queryon to invenoty Database with parameters of product inv."""
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM purchases')

            cursor.execute(data)
            return cursor.fetchall()
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()


# Database.initialize()