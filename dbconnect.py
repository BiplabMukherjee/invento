import mysql.connector


class dbconnect:

    def connect(self):
        conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            passwd="",
            database="invento"
        )
        if(conn):
            print("Connectin Established")

# dbcursor = conn.cursor()
