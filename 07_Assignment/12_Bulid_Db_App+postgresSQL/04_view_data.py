import psycopg2

conn = psycopg2.connect(
            host="localhost",      
            port="5432",           
            database="postgres",    
            user="postgres",    
            password="123456" 
        )

cursor = conn.cursor()
cursor.execute('''Select * from employees;''')
data = cursor.fetchall()
print("Data of Employees table : ",data)

conn.commit()
conn.close()