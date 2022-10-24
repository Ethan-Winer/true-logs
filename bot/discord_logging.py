import sqlite3
import time


class Logs:
    def __init__(self):
        # self.server_db = sqlite3.connect('../database/server.db')
        self.db = sqlite3.connect(':memory:')
        self.db.execute('PRAGMA foreign_keys = ON')
        self.cursor = self.db.cursor()
        self.cursor.execute(""" CREATE TABLE guilds (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL
                                    )""")

        self.cursor.execute(""" CREATE TABLE channels (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL
                                )""")

        self.cursor.execute(""" CREATE TABLE messages (
                                        id INTEGER PRIMARY KEY,
                                        created_at INTEGER NOT NULL,
                                        author TEXT NOT NULL,
                                        content TEXT NOT NULL
                                )""")

        # self.cursor.execute("""INSERT INTO guilds
        #                                 (id, name)
        #                                 VALUES
        #                                 (10,'yaaay server')""")

        self.db.commit()

        # self.cursor.execute("SELECT * FROM guilds")

        # rows = self.cursor.fetchall()

        # print(rows)

    def log_message(self, message):
        self.cursor.execute(f'SELECT * FROM guilds WHERE id={message.guild.id}')
        # guild = self.cursor.fetchone()
        # print(f'fetch one with id: {self.cursor.fetchone()}')
        # print(f'fetch one with id: {self.cursor.fetchone()}')
        # print(f'fetch one with id: {self.cursor.fetchone()}')

        # print(guild is None)
        # print(f'fetch one with id: {guild}')
        # print(f'fetch one with id: {guild}')
        # print(f'fetch one with id: {guild}')

        # print(f'fetch one result length: {self.cursor.fetchone()}')
        # print(f"fetch all: {self.cursor.execute('SELECT * FROM guilds').fetchall()}")
        # print(guild)

        if self.cursor.fetchone() is None:
            print('here')
            self.cursor.execute(f"""INSERT INTO guilds 
                                            (id,name)
                                            VALUES
                                            ({message.guild.id},'{message.guild.name}')""")
            print('added server')

        self.cursor.execute(f'SELECT * FROM channels WHERE id = {message.channel.id}')
        if self.cursor.fetchone() is None:
            self.cursor.execute(f"""INSERT INTO channels
                                            (id,name)
                                            VALUES
                                            ({message.channel.id},'{message.channel.name}')""")
            print('channel added')

        self.cursor.execute(f"INSERT INTO messages (id,created_at,author,content) VALUES ({message.id},{message.created_at.timestamp()},'{message.author.name}','{message.content}')")

        self.cursor.execute('SELECT * FROM messages ORDER BY created_at DESC LIMIT 5')
        messages = self.cursor.fetchall()
        
        # self.cursor.execute('SELECT * FROM ')
        self.db.commit();

        print(messages)