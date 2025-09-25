import psycopg2

conn = psycopg2.connect(
            host="localhost",      
            port="5432",           
            database="postgres",    
            user="postgres",    
            password="123456" 
        )

cursor = conn.cursor()
cursor.execute('''Insert Into employees(Name,Id,Age) values('Sohan',001,46);''')
print("Insert Data of emp into Employees Table successfully.")

conn.commit()
conn.close()