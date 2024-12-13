import sqlite3


class DBManager:
    def __init__(self):
        self.connection = sqlite3.connect("report.db")
        self.cursor = self.connection.cursor()

        self.add_table()

    def add_table(self):
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

    def add_report(self, data: dict):
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


# data = {
#     "file_hash": "f6a8e89b28c62c1c8e4f36c2e1e5a4a5e7b8e8c9d4f2a7c3b2e1f4d5c8b7a6e2",
#     "analysis": "23/45 Malicious",
#     "community_score": 85,
#     "file_type": "PE32 executable",
#     "file_size": 456789,
#     "file_name": "example_file.exe",
#     "file_last_analysis": "2024-12-03 15:30:00",
# }

# db_manager = DBManager()

# db_manager.add_table()
# db_manager.add_report(data=data)

# db_manager.save_db()
