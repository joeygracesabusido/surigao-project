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
                    "CREATE TABLE IF NOT EXISTS inventory (id INT AUTO_INCREMENT PRIMARY KEY,\
                            store_id VARCHAR(100),\
                                product_id VARCHAR(100), \
                                    quantity_inv DECIMAL(9,2)) \
                                        ")

except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")

try:
    cursor.execute(
                    "CREATE TABLE IF NOT EXISTS sales (id INT AUTO_INCREMENT PRIMARY KEY,\
                            store_id VARCHAR(100),\
                                product_id VARCHAR(100), \
                                    sales_inv DECIMAL(9,2))\
                                        ")

except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")


def selection():

    print('===================================')
    print('1001- Insert Inventory')
    print('1002- Insert Sales')
    print('1003- Report')
    print('x-Exit')

    ans = input('Please enter code for your Desire transactio: ')

    if ans == '1001':
        return insert_inventory()
    elif ans == '1002':
        return insert_sale()
    elif ans == '1003':
        return reportInventory()
    elif ans =='Exit':
        exit

    print('===================================')

def insert_inventory():
    mydb._open_connection()
    cursor = mydb.cursor()
    
    store_id = input("Enter Store ID: ")
    product_id = input("Enter Product ID: ")
    quantity_inv = input('Enter quantity: ')

    try:
        cursor.execute("INSERT INTO inventory (store_id,"
                           "product_id,quantity_inv)"
                           
                           " VALUES(%s, %s, %s)",

                           (store_id, product_id, quantity_inv))

        mydb.commit()
        mydb.close()
        cursor.close()
        selection()
   
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")

def insert_sale():
    mydb._open_connection()
    cursor = mydb.cursor()
    
    store_id = input("Enter Store ID: ")
    product_id = input("Enter Product ID: ")
    quantity_inv = input('Enter Sales: ')

    try:
        cursor.execute("INSERT INTO sales (store_id,"
                           "product_id,sales_inv)"
                           
                           " VALUES(%s, %s, %s)",

                           (store_id, product_id, quantity_inv))

        mydb.commit()
        mydb.close()
        cursor.close()
        selection()
   
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")

def reportInventory():
    """
    """
    mydb._open_connection()
    cursor = mydb.cursor()

    cursor.execute("SELECT I.store_id, I.product_id, I.quantity_inv, S.sales_inv, (sum(I.quantity_inv) - sum(S.sales_inv)) AS remaining \
                    FROM sales S INNER JOIN inventory I \
                    ON I.store_id = S.store_id \
                    AND I.product_id = S.product_id \
                    GROUP BY I.store_id,I.quantity_inv,S.sales_inv,I.product_id,S.product_id\
                    ")
    # cursor.execute("SELECT \
    #                     I.store_id \
    #                     , I.product_id \
    #                     , COALESCE(( \
    #                             SELECT \
    #                                 SUM(sales_inv) \
    #                             FROM sales S \
    #                             WHERE S.store_id = I.store_id \
    #                                 AND S.product_id = I.product_id \
    #                     ), 0) AS SALES \
    #                     , I.quantity_inv - COALESCE(( \
    #                             SELECT \
    #                                 SUM(sales) \
    #                             FROM sales S \
    #                             WHERE S.store_id = I.store_id \
    #                                 AND S.product_id = I.product_id \
    #                     ), 0) AS REMAINING \
    #                 FROM inventory AS I \
    #                 \
    #                 ORDER BY \
    #                     I.store_id \
    #                     , I.product_id")

    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['Store','Product ID','Quantity Inv',
                                    'Sales Inv.','Remaining Bal.'], tablefmt='psql'))
    selection()

selection()