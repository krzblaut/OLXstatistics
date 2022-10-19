import pyodbc
import time


class DbConnect:
    """class created for handling database interaction"""

    def __init__(self, driver, server, database):
        self.connection = None
        self.driver = driver
        self.server = server
        self.database = database

    def get_connection(self):
        """getting connected with database"""
        try:
            self.connection = pyodbc.connect(f'Driver={self.driver};'
                                             f'Server={self.server};'
                                             f'Database={self.database};'
                                             'Trusted_Connection=yes;')
            print("Database connected successfully.")
        except pyodbc.Error as e:
            print(f"An Error has occurred: {e}")
        # return connection

    def check_exists(self, query):
        """checks if record already exists in database"""
        cursor = self.connection.cursor()
        exists = False
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            if len(data) != 0:
                exists = True
        except pyodbc.Error as e:
            print(f" Query Failed……{e}")
        return exists

    def insert_data(self, sql_query, values):
        """ inserts values to database """
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql_query, values)
            self.connection.commit()
        except pyodbc.Error as e:
            sqlstate = e.args[0]
            if sqlstate == '23000':
                pass
            else:
                print(f" Query Failed……{e}")

    def get_data(self, query):
        """pulls data out of database"""
        records = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
        except pyodbc.Error as e:
            print(f" Query Failed……{e}")
        for row in rows:
            records.append(row)
        return records
