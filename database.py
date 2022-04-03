import mysql.connector
from mysql.connector import Error

def Connexion(liste)-> list:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='user',
                                            user='root',
                                            password='')

        sql_select_Query = f"select * from Users where mail = '{liste[0]}' AND password = '{liste[1]}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        return cursor.rowcount == 1

    except mysql.connector.Error as e:
        return False


