from database_login import Database
from insert_login import Login
# from insert_login import Login

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
    
    
    
# deleteUser()
# insertLogin()

test2('joeysabusido')

# test()
    