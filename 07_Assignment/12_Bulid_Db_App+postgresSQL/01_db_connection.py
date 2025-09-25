import psycopg2
from psycopg2 import sql, extras

def connect_db():
    try:
        # Connection parameters
        conn = psycopg2.connect(
            host="localhost",      
            port="5432",           
            database="postgres",    
            user="postgres",      
            password="123456" 
        )

        # Create a cursor
        cursor = conn.cursor()

        # Example query
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("Connected to:", db_version)
        
        

        # Always close
        cursor.close()
        conn.close()

    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)

if __name__ == "__main__":
    connect_db()
