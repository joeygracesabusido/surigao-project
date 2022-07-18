from database_login import Database
from insert_login import Login
from datetime import date
# from insert_login import Login
from equipment_database import Database
Database.initialize()


@staticmethod
def test():
    username ='joeysabusido'
    password = 'genesis@11'
    # table='admin_login'
    data = Database.login_credentials(username=username,password=password)

    for i in data:
        print(i)



def test2(test):
        table='admin_login'
    
        data = Database.login_credentials2(table=table)

        user = []
        for i in data:
            user.append(i[2])

        print(test if test in user else 'not in user')





@staticmethod
def insertLogin():
    table = 'admin_login'
    fullname = input("Enter fullname :") 
    username = input("Enter Username :") 
    password = input('enter password: ')
    status = input('Enter Status approval:')

    

    data =Login(fullname,username, password, status)
    data.test_insert()

    

@staticmethod
def deleteUser():
    
    table = 'admin_login'
    id = input("Enter ID :") 

    data =Database.delete_user(table=table,id=id)


@staticmethod
def equipmentList(): 
    table = 'equipment'
    
    data = Database.select_all_equipment(table=table)

    print(data)
    # cnt = 0
    # for row in myresult:
    #     cnt+=1
    #     equipmentID = row[1]
    #     chases_number = row[3]
    #     plate_number = row[4]   
    #     print(row)

@staticmethod

def select_one(): 
    id = 1
    equipmentid = input('Enter Equipment ID: ')
    
    data = Database.selectEquipment(equipmentID=equipmentid)

    print(data)

@staticmethod
def delete_equipment():
    
    table = 'equipment'
    id = input("Enter ID :") 

    data =Database.delete_equipment(table=table,id=id)

@staticmethod
def testing_date():
    now = date.today()
    print(now)
# delete_equipment()
# select_one()
# equipmentList()    
# deleteUser()
# insertLogin()

# test2('joeysabusido')

# test()
testing_date()
    