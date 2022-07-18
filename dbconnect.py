import mysql.connector


class Dbconnect:

    def connect(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            passwd="",
            database="invento"
        )
        if(self.conn):
            print("Connectin Established")
            return self.conn

    def closeconn(self):
        self.conn.close()
        print("Connection Closed")
        # dbcursor = conn.cursor()
