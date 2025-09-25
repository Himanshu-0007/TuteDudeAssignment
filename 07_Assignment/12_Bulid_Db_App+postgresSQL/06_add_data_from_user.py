import psycopg2

connection =  psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "123456",
    port = "5432"
)

def insertDataByuser():
    try:
        cursur = connection.cursor()
        print("Database connection established.")
        
        intCnt = 1
        
        while intCnt <= 2:          
            name = input("Enter name : ")
            id = input("Enter Id number : ")
            age = input("Enter age : ")
            
            query = '''Insert Into employees(Name,Id,Age) values(%s,%s,%s);'''
            cursur.execute(query , (name,id,age))          
            
            intCnt += 1
            
        cursur.execute('''Select * from employees;''')
        data = cursur.fetchall()    
        print("Employees data is : ",data)
        connection.commit()
        connection.close()        
    except  Exception as e:
        print("Error while connecting to PostgreSQL:", e)
        
insertDataByuser()        