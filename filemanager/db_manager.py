import sqlite3
from helper import Helper

class DBManager:

    def __init__(self, analysis_mode):
        self.connection = sqlite3.connect("report.db")
        self.cursor = self.connection.cursor()
        self.mode = analysis_mode
        self.helper = Helper()
        self.add_table()

    def add_table(self):

        if self.mode == "file":
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS records (
                    hash TEXT PRIMARY KEY NOT NULL,
                    positives TEXT NOT NULL,
                    community_score INTEGER NOT NULL,
                    file_type TEXT NOT NULL,
                    file_size TEXT NOT NULL,
                    file_name TEXT NOT NULL,
                    last_analysis TEXT NOT NULL)
                """
            )

        elif self.mode == "url":
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS records (
                    url TEXT PRIMARY KEY NOT NULL,
                    positives TEXT NOT NULL,
                    community_score INTEGER NOT NULL,
                    creation_date TEXT NOT NULL,
                    registrar TEXT NOT NULL,
                    last_analysis TEXT NOT NULL)
                """
            )

        elif self.mode == "ip":
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS records (
                    ip TEXT PRIMARY KEY NOT NULL,
                    analysis TEXT NOT NULL,
                    country INTEGER NOT NULL,
                    last_analysis TEXT NOT NULL,
                    community_score TEXT NOT NULL)
                """
            )

    def add_report(self, data: dict):
        
        if self.mode == "url":
            fields = self.helper.get_data_fields(data=data, mode=self.mode)
            only_values = [fields[1] for i in fields]

            query = "INSERT INTO records (url, positives, community_score, creation_date, registrar, last_analysis) VALUES (?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, fields)

        elif self.mode == "file":
            
            fields = self.helper.get_data_fields(data=data, mode=self.mode)
            only_values = [i[1] for i in fields]
            print(only_values)

                
            query = "INSERT INTO records (hash, positives, community_score, file_type, file_size, file_name, last_analysis) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, only_values)

        elif self.mode == "ip":

            fields = self.helper.get_data_fields(data=data, mode=self.mode)
            only_values = [i[1] for i in fields]
            print(only_values)

                
            query = "INSERT INTO records (ip, analysis, country, last_analysis, community_score) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(query, only_values) 

    def commit_db(self):
        self.connection.commit()

    def close_db(self):
        self.connection.close()

    def save_db(self):
        self.commit_db()
        self.close_db()

