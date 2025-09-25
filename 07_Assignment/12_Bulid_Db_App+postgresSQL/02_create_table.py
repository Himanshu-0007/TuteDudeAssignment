import psycopg2

conn = psycopg2.connect(
            host="localhost",      
            port="5432",           
            database="postgres",    
            user="postgres",    
            password="123456" 
        )

cursor = conn.cursor()
cursor.execute('''CREATE TABLE employees(Name Text, Id int, Age int);''')
print("Create Employees Table successfully.")

conn.commit()
conn.close()