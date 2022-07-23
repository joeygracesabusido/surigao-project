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

        try: 
            cursor.execute(
                    "CREATE TABLE IF NOT EXISTS equipment (id INT AUTO_INCREMENT PRIMARY KEY,\
                            equipment_id VARCHAR(100),\
                                equipment_name VARCHAR(100), \
                                    purchase_price VARCHAR(100), \
                                        chases_number VARCHAR(100),\
                                            plate_number VARCHAR(50),\
                                                date_purchase date DEFAULT NULL, \
                                               UNIQUE (equipment_id))ENGINE = InnoDB;")
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def insert_equipment(equipmentID,equipment_name,
                                purchase_price,chases_number,
                                plate_number,date_purchase):
        """
        this function is to insert
        equipment in 
        """ 
        Database.DATABASE._open_connection()
        try:
           
            data = ( "INSERT INTO equipment (equipment_id,equipment_name,\
                                purchase_price,chases_number,plate_number,date_purchase)"
                    "VALUES(%s,%s,%s,%s,%s,%s)")
            val = (equipmentID,equipment_name,purchase_price,chases_number,
                            plate_number,date_purchase)
            #                  
            # cursor.execute(data)              
            cursor.execute(data,val) 
           
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:

            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def selectEquipment(equipmentID):
        """
        This function is for selecting
        equipment with parameters of equipment
        so that it will not duplicate Number
        """
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM equipment\
                 WHERE equipment_id = %s ')
                #  WHERE equipment_id LIKE '+equipmentID+'
            val =(equipmentID,)
                                          
            cursor.execute(data,val)
            return cursor.fetchone()

        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()


    @staticmethod
    def select_all_equipment(table):
        """
        This function is for selecting
        equipment with parameters of equipment
        so that it will not duplicate Number
        """
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM   '+table+' ')               
            cursor.execute(data)
            return cursor.fetchall()

        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            
            Database.DATABASE.close()

    @staticmethod
    def delete_equipment(table,id):
        """
        This function is 
        to insert data to admin login
        """
        Database.DATABASE._open_connection()
        try:
            
            data = ('DELETE  FROM   '+table+' \
                WHERE id = "'+id+'"')       
            #                  
            # cursor.execute(data)              
            cursor.execute(data) 
            
            return ("Data has been deleted")
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def select_one_equipment(id):
        """
        This function is for querying with parameters of ID
        """
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM equipment \
                WHERE id = "'+id+'"')

            cursor.execute(data)
            return cursor.fetchall()
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

    @staticmethod
    def update_one_equipment(equipmentID,equipment_name,
                            purchase_price,chases_number,
                            plate_number,date_purchase,id):
        """
        This function is to update Equipment with parameters of Trans ID
        """
        try:
            data = ('UPDATE equipment SET equipment_id=%s,\
                    equipment_name=%s,purchase_price=%s, \
                     chases_number=%s,plate_number=%s,date_purchase=%s  \
                        WHERE id = %s')
            val =(equipmentID,equipment_name,purchase_price,chases_number,
                    plate_number,date_purchase,id)
            cursor.execute(data,val)
           
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            Database.DATABASE.commit()
            Database.DATABASE.close()

# Database.initialize()  