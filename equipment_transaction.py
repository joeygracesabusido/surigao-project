from typing import List
from xml.dom.minidom import Element
from equipment_database import Database
from dataclasses import dataclass,field

from tabulate import tabulate

Database.initialize()
# cursor= Database.DATABASE.cursor()

@dataclass
class Equipment(object):
    equipmentID: str
    equipment_name: str
    purchase_price: float
    chases_number: str
    plate_number: str
    date_purchase: str
    search_string: str = field(init=False)

    def __post_init__(self) -> None:
        self.search_string = f"{self.equipmentID} {self.equipment_name}"
        
        
    
    # def __init__(self,equipmentID,equipment_name,purchase_price,chases_number,
    #                             plate_number,date_purchase):
      
    #     self.equipmentID = equipmentID
    #     self.equipment_name = equipment_name
    #     self.purchase_price = purchase_price
    #     self.chases_number = chases_number
    #     self.plate_number = plate_number
    #     self.date_purchase = date_purchase
    

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
    
        

    def main() :
        test1 = Database.select_all_equipment(table='equipment')
       
                
        print(tabulate(test1, headers =['Id','Equipment ID',
                                        'Equipment Name','Purchase Price','Chases Number',
                                        'Plate Number','Date Purchase','Search Value'], tablefmt='psql'))
        equipmentID = ""
        equipment_name = ""
        purchase_price = 0
        chases_number = ""
        plateNumber = ""
        date_purchase = ""
        for i in test1:
            equipmentID = i[1]
            equipment_name = i[2]
            purchase_price = i[3]
            chases_number = i[4]
            plateNumber = i[5]
            date_purchase = i[6]

            test = Equipment(equipmentID = equipmentID,equipment_name=equipment_name,
                            purchase_price=purchase_price,chases_number=chases_number,
                            plate_number=plateNumber,date_purchase=date_purchase)
            print(test)
        # print(test.__dict__['equipmentID'])
        # print(test)
            
        # equipID = input("Enter equipment ID:  ")
        # equipment_name = input("Enter equipment Name:  ")
        # purchase_amount  = input("Enter pruchase Amount  ")
        # chases_number = input("Enter chases Number:  ")
        # plate_number = input("Enter Plate Number:  ")
        # date_purchase = input("Enter date Purchases:  ")

        # data2 = Equipment(equipmentID = equipID, equipment_name=equipment_name,
        #                 purchase_price=purchase_amount,
        #                 chases_number=chases_number,
        #                 plate_number = plate_number,
        #                 date_purchase=date_purchase)
        # print(data2)

if __name__ == '__main__':
    Equipment.main()




   


        