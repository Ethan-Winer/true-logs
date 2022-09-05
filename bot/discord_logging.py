import sqlite3

class Logs:
    def __init__(self):
        self.server_db = sqlite3.connect('../database/server.db')
        

    def log_message(message):
        return