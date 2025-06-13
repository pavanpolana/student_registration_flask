import mysql.connector
def connection_db():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vivekanda@123",
        database="student_db2"
        )
    return conn