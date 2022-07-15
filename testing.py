from pickle import NONE
from dataclasses import dataclass
import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
                                host="192.46.225.247",
                                user="joeysabusido",
                                password="Genesis@11",
                                database="ldsurigao",
                                auth_plugin='mysql_native_password')
cursor = mydb.cursor()
try:
    cursor.execute(
                    """CREATE TABLE IF NOT EXISTS inventory (id INT AUTO_INCREMENT PRIMARY KEY,
                            date DATE,
                            product_id VARCHAR(100), 
                            quantity DECIMAL(9,2) ,
                            FOREIGN KEY (product_id) REFERENCES inventory_onhand(product_id)) 
                                        """)

except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")

try:
    cursor.execute(
                    """CREATE TABLE IF NOT EXISTS sales (id INT AUTO_INCREMENT PRIMARY KEY,
                            date DATE,
                            product_id VARCHAR(100), 
                            quantity DECIMAL(9,2),
                            FOREIGN KEY (product_id) REFERENCES inventory_onhand(product_id))
                                        """)

except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")

try:
    cursor.execute(
                    """CREATE TABLE IF NOT EXISTS inventory_onhand (id INT AUTO_INCREMENT PRIMARY KEY,
                            product_id VARCHAR(100), 
                            description VARCHAR(250),
                            quantity DECIMAL(9,2),
                            UNIQUE (product_id))
                                        """)

except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")


def selection():

    print('===================================')
    print('1001- Insert On Hand')
    print('1002- Insert Inventory')
    print('1003- Insert Sales')
    print('1004- Report')
    print('1005- Update On Hand')
    print('x-Exit')

    ans = input('Please enter code for your Desire transactio: ')

    if ans == '1001':
        return insert_inventoryOnHand()
    elif ans == '1002':
        return insert_inventory()
    elif ans == '1003':
        return insert_sale()
    elif ans == '1004':
        return reportInventory()
    elif ans == '1005':
        return update_inventoryOnhand()
    elif ans =='Exit':
        exit

    print('===================================')
def insert_inventoryOnHand()-> None:
    """This function is for inserting inventory on Hand Table"""
    mydb._open_connection()
    cursor = mydb.cursor()

    product_id = input("Enter Product ID: ")
    description = input("Enter description: ")
    quantity_inv = input('Enter quantity: ')

    try:
        cursor.execute("INSERT INTO inventory_onhand (product_id,"
                           "description,quantity)"
                           
                           " VALUES(%s, %s, %s)",

                           (product_id, description, quantity_inv))

        
   
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")
    finally:
        mydb.commit()
        mydb.close()
        cursor.close()

    selection()



def insert_inventory():
    """This function is to insert inventory add"""
    mydb._open_connection()
    cursor = mydb.cursor()

    product_id = ""
    
    date = input("Enter Date: ")
    product_id = input("Enter Product ID: ")
    quantity_inv = input('Enter quantity: ')

    cursor.execute("Select quantity from inventory_onhand WHERE product_id = '" + product_id + "' ")

    myresult = cursor.fetchall()

    totalQuantity_update = 0
    totalQuantity_update2 = ''
    for i in myresult:
        totalQuantity = i[0]
        totalQuantity_update = float(quantity_inv) + float(totalQuantity)
        totalQuantity_update2 = str(totalQuantity_update)
        

    

    try:
        cursor.execute("INSERT INTO inventory (date,"
                        "product_id,quantity)"
                        
                        " VALUES(%s, %s, %s)",

                        (date, product_id, quantity_inv))

        
      

        

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")
    finally:
        mydb.commit()
        mydb.close()
        cursor.close()

    mydb._open_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(
        "UPDATE inventory_onhand SET quantity = '" + totalQuantity_update2 + "'"\
        "WHERE product_id = '" + product_id + "'")
        

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")
    finally:
        mydb.commit()
        mydb.close()
        cursor.close()

    selection()

def insert_sale():
    """This function is for inventory withdrawal"""
    mydb._open_connection()
    cursor = mydb.cursor()
    
    product_id = ""
    date = input("Enter Date: ")
    product_id = input("Enter Product ID: ")
    quantity_inv = input('Enter quantity: ')

    cursor.execute("Select quantity from inventory_onhand WHERE product_id = '" + product_id + "' ")

    myresult = cursor.fetchall()

    totalQuantity_update = 0
    totalQuantity_update2 = ''
    for i in myresult:
        totalQuantity = i[0]
        totalQuantity_update = float(totalQuantity) - float(quantity_inv)  
        totalQuantity_update2 = str(totalQuantity_update)


    try:
        cursor.execute("INSERT INTO sales (date,"
                        "product_id,quantity)"
                        
                        " VALUES(%s, %s, %s)",

                        (date, product_id, quantity_inv))

       
    
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")
    finally:
        mydb.commit()
        mydb.close()
        cursor.close()

    # this is to update invenotry on Hand
    mydb._open_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(
        "UPDATE inventory_onhand SET quantity = '" + totalQuantity_update2 + "'"\
        "WHERE product_id = '" + product_id + "'")
        

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")
    finally:
        mydb.commit()
        mydb.close()
        cursor.close()

    selection()
def reportInventory():
    """
    """
    mydb._open_connection()
    cursor = mydb.cursor()

    

    cursor.execute("""
                    Select * from inventory_onhand
                """)

    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID','Product ID','Description','Quantity'], tablefmt='psql'))
    selection()

def update_inventoryOnhand():
    """
    This is for querying inventory Balance
    this is trial only
    """
    mydb._open_connection()
    cursor = mydb.cursor()

    product_id = input("Enter Product ID: ")
    quantity_inv = input('Enter quantity: ')

    cursor.execute(
        "UPDATE inventory_onhand SET quantity = '" + quantity_inv + "'"\
        "WHERE product_id = '" + product_id + "'")

def report_sales_Inventory():
    """
    """
    mydb._open_connection()
    cursor = mydb.cursor()

    

    cursor.execute("""
                    Select product_id from sales
                """)

    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID','Product ID','Description','Quantity'], tablefmt='psql'))
    selection()       

report_sales_Inventory()
# selection()