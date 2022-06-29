from typing import List
from equipment_database import Database
from dataclasses import dataclass,field

Database.initialize()
# cursor= Database.DATABASE.cursor()


class Equipment(object):
    
    def __init__(self,equipmentID,equipment_name,purchase_price,chases_number,
                                plate_number,date_purchase):
      
        self.equipmentID = equipmentID
        self.equipment_name = equipment_name
        self.purchase_price = purchase_price
        self.chases_number = chases_number
        self.plate_number = plate_number
        self.date_purchase = date_purchase
    

    # @staticmethod
    def equipment_insert(self):
        """
        This function is 
        to insert data to admin login
        """
        Database.insert_equipment(equipmentID= self.equipmentID, equipment_name=self.equipment_name,
                        purchase_price=self.purchase_price,
                        chases_number=self.chases_number,
                        plate_number=self.plate_number,
                        date_purchase=self. date_purchase)



   


        