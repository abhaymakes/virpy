import sqlite3


class DBManager:

    def __init__(self, analysis_mode):
        self.connection = sqlite3.connect("report.db")
        self.cursor = self.connection.cursor()
        self.mode = analysis_mode
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

    def add_report(self, data: dict):
        
        if self.mode == "url":
            fields = [
                data.get("url", "N/A"),
                data.get("analysis", "N/A"),
                str(data.get("community_score", "N/A")),
                str(data.get("creation_date", "N/A")),
                str(data.get("registrar", "N/A")),
                data.get("last_analysis", "N/A")
            ]

            query = "INSERT INTO records (url, positives, community_score, creation_date, registrar, last_analysis) VALUES (?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, fields)

        elif self.mode == "file":
            fields = [
                data.get("file_hash", "N/A"),
                data.get("analysis", "N/A"),
                str(data.get("community_score", "N/A")),
                str(data.get("file_type", "N/A")),
                str(data.get("file_size", "N/A")),
                data.get("file_name", "N/A"),
                data.get("file_last_analysis", "N/A")
            ]
                
            query = "INSERT INTO records (hash, positives, community_score, file_type, file_size, file_name, last_analysis) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, fields)

    def commit_db(self):
        self.connection.commit()

    def close_db(self):
        self.connection.close()

    def save_db(self):
        self.commit_db()
        self.close_db()

