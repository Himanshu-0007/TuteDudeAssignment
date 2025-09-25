import psycopg2

conn = psycopg2.connect(
            host="localhost",      
            port="5432",           
            database="postgres",    
            user="postgres",    
            password="123456" 
        )

cursor = conn.cursor()
cursor.execute('''truncate table employees;''')

cursor.execute('''Select * from employees;''')
data = cursor.fetchall()
print("Delete Data of Employees table : ", len(data) == 0)

conn.commit()
conn.close()