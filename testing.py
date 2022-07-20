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
# try:
#     cursor.execute(
#                     """CREATE TABLE IF NOT EXISTS inventory (id INT AUTO_INCREMENT PRIMARY KEY,
#                             date DATE,
#                             product_id VARCHAR(100), 
#                             quantity DECIMAL(9,2) ,
#                             FOREIGN KEY (product_id) REFERENCES inventory_onhand(product_id)) 
#                                         """)

# except Exception as ex:
#             print("Error", f"Error due to :{str(ex)}")

# try:
#     cursor.execute(
#                     """CREATE TABLE IF NOT EXISTS sales (id INT AUTO_INCREMENT PRIMARY KEY,
#                             date DATE,
#                             product_id VARCHAR(100), 
#                             quantity DECIMAL(9,2),
#                             FOREIGN KEY (product_id) REFERENCES inventory_onhand(product_id))
#                                         """)

# except Exception as ex:
#             print("Error", f"Error due to :{str(ex)}")

# try:
#     cursor.execute(
#                     """CREATE TABLE IF NOT EXISTS inventory_onhand (id INT AUTO_INCREMENT PRIMARY KEY,
#                             product_id VARCHAR(100), 
#                             description VARCHAR(250),
#                             quantity DECIMAL(9,2),
#                             UNIQUE (product_id))
#                                         """)

# except Exception as ex:
#             print("Error", f"Error due to :{str(ex)}")


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
def insert_inventoryOnHand():
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

def insertCategory():
    """This function is to insert to category Table"""
    mydb._open_connection()
    cursor = mydb.cursor()

    category_list = input("Enter Category: ") 
    try: 
        data = "INSERT INTO category (category) VALUES(%s)"
                        
        val =  category_list

        cursor.execute(data,(val,))

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")
    finally:

        mydb.commit()
        mydb.close()

def inve_category():
    """This function is for Displaying inventory category"""
    from inventory_database import Database
    Database.initialize()
    agg_result = Database.select_all_category_from_category()
   
    for i in agg_result:
        print(i)

def inventory_treevie_list():
        """This function is for querying for treeview for inventory Database"""
        from inventory_database import Database
        Database.initialize()   

        myresult = Database.select_all_from_inventoryData()

        for i in myresult:
            productID_view = i[1]   
            brand_view = i[2]   
            description_view = i[3]  
            quantity_view = i[4] 

            print(productID_view)

def search_inventory():
    """This is to search invenotry using product ID"""
    from inventory_database import Database
    Database.initialize()

    productId_search = input("Enter inventory ID: ")
    myresult = Database.select_One_from_inventoryData(product_id=productId_search)

    for i in myresult:
        brandSearch = i[2]
        print(brandSearch)
        
        
# inventory_treevie_list()
    # data = []
    # for x in agg_result:
    #     data.append(x[0])
    # print(data)

# inve_category()
# insertCategory()
# report_sales_Inventory()
# selection()

search_inventory()
