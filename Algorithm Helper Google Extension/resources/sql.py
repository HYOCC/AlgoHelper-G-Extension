import mysql.connector
import bcrypt
import secrets

# Connects to the database
conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'Oscarsgyang123',
    database = 'users'
)

# Creates the cursor
cursor = conn.cursor()

def register_user(username:str, password:str):
    question_key = secrets.token_hex()
    
    query = 'INSERT INTO user_info (user, password, question_key) VALUES (%s, %s, %s)'
    values = (username, password, question_key)
    cursor.execute(query, values)
    
    query = 'INSERT INTO question_code (question_key) VALUES (%s)'
    values = (question_key)
    cursor.execute(query, values)
    
    conn.commit() 
    conn.close()
    

