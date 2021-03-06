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

        # try: 
        #     cursor.execute(
        #             "CREATE TABLE IF NOT EXISTS equipment (id INT AUTO_INCREMENT PRIMARY KEY,\
        #                     equipment_id VARCHAR(100),\
        #                         equipment_name VARCHAR(100), \
        #                             purchase_price VARCHAR(100), \
        #                                 chases_number VARCHAR(100),\
        #                                     plate_number VARCHAR(50),\
        #                                         date_purchase date DEFAULT NULL, \
        #                                        UNIQUE (equipment_id))ENGINE = InnoDB;")
        # except Exception as ex:
        #     print("Error", f"Error due to :{str(ex)}")
        # finally:
        #     Database.DATABASE.commit()
        #     Database.DATABASE.close()
        # Database.DATABASE._open_connection()
        # try: 
        #     cursor.execute(
        #             """CREATE TABLE IF NOT EXISTS equipment_status (id INT AUTO_INCREMENT PRIMARY KEY,
        #                     equipment_id VARCHAR(100),
        #                     status VARCHAR(100), 
        #                     date date DEFAULT NULL,
        #                     work_update VARCHAR(350),
        #                     time_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        #                     INDEX (equipment_id), 
        #                     CONSTRAINT FK_equipmentStatus FOREIGN KEY (equipment_id) 
        #                     REFERENCES equipment(equipment_id) ON UPDATE CASCADE ON DELETE CASCADE,
        #                     UNIQUE (equipment_id))ENGINE = InnoDB;""")
        # except Exception as ex:
        #     print("Error", f"Error due to :{str(ex)}")
        # finally:
        #     Database.DATABASE.commit()
        #     Database.DATABASE.close()
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
        Database.DATABASE._open_connection()
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

# ================================================Equipment Status Back End========================================
    @staticmethod
    def insert_equipmentStatus(equipment_id,status,
                                date,work_update,
                                ):
        """
        this function is to insert
        equipmentstatus
        """ 
        Database.DATABASE._open_connection()
        try:
           
            data = ( "INSERT INTO equipment_status (equipment_id,status,\
                                date,work_update)"
                    "VALUES(%s,%s,%s,%s)")
            val = (equipment_id,status,date,work_update)
            #                  
            # cursor.execute(data)              
            cursor.execute(data,val) 
           
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:

            Database.DATABASE.commit()
            Database.DATABASE.close()
    
    @staticmethod
    def search_one_equipmentStatus(id):
        """
        this function is to query using ID from equipment_status
        """ 
        Database.DATABASE._open_connection()
        try:
           
            data = ( "Select * from equipment_status \
                        Where id = %s")
            val = (id)
            #                  
            # cursor.execute(data)              
            cursor.execute(data,(val,)) 
            return cursor.fetchall()
           
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:

            
            Database.DATABASE.close()
    
    @staticmethod
    def update_equipmentStatus(equipment_id,status,
                                work_update,time_update,id):
        """This function is for updating record to database"""
        Database.DATABASE._open_connection()
        try:
            data = ("""
                    UPDATE equipment_status set equipment_id=%s,
                    status=%s,work_update=%s,time_update=%s
                    WHERE id = %s
                    """)

            val = (equipment_id,status,work_update,time_update,id)

            cursor.execute(data,val)

        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:

            Database.DATABASE.commit()
            Database.DATABASE.close()


    @staticmethod
    def select_all_equipmentStatus():
        """This function si to query all from equipment_status """
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM equipment_status ')               
            cursor.execute(data)
            return cursor.fetchall()

        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            
            Database.DATABASE.close()   

    @staticmethod
    def select_status_equipmentStatus(status):
        """This function si to query all from equipment_status """
        Database.DATABASE._open_connection()
        try:
            data = ('SELECT * FROM equipment_status  where status = "'+status+'" ')               
            cursor.execute(data)
            return cursor.fetchall()

        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")
        finally:
            
            Database.DATABASE.close()   



# Database.initialize()  