from database_login import Database
from insert_login import Login
# from insert_login import Login

Database.initialize()


@staticmethod
def test():
    username ='joeysabusido'
    password = 'genesis@11'
    table='admin_login'
    data = Database.login_credentials(table=table,username=username,password=password)

    for i in data:
        print(i)

@staticmethod
def test2():
    table='admin_login'
    
    data = Database.login_credentials2(table=table)

    for i in data:
        print(i)



@staticmethod
def insertLogin():
    table = 'admin_login'
    username = input("Enter Username :") 
    password = input('enter password: ')
    status = input('Enter Status approval:')

    

    data =Login(username, password, status)
    data.test_insert()
    
    

insertLogin()

# test2()
    