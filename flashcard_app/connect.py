import mysql.connector

def set_db(query):
    connect = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="flashcard"
    )
    cursor = connect.cursor()
    cursor.execute(query)
    connect.commit()
    connect.close()
    
def get_db(query):
    connect = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="flashcard"
    )
    cursor = connect.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    connect.commit()
    connect.close()
    return data




