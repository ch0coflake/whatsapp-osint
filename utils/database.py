import sqlite3

class Database():
    def create_table():
        conn = sqlite3.connect('database/database.db')
        c = conn.cursor()
        c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Users'")
        table_exists = c.fetchone()[0]
        if not table_exists:
            c.execute('CREATE TABLE Users (name TEXT PRIMARY KEY)')
        conn.commit()
        conn.close()

        conn = sqlite3.connect('database/database.db')
        c = conn.cursor()
        c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Connections'")
        table_exists = c.fetchone()[0]
        if not table_exists:
            c.execute('CREATE TABLE Connections (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, date TEXT, hour TEXT, minute TEXT, second TEXT, type_connection TEXT, time_connected TEXT, FOREIGN KEY (user_name) REFERENCES Usuarios(name))')
        conn.commit()
        conn.close()

    def insert_user(name):
        conn = sqlite3.connect('database/database.db')
        c = conn.cursor()
        c.execute('INSERT OR IGNORE INTO Users (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    def insert_connection_data(name, date, hour, minute, second, type_connection):
        conn = sqlite3.connect('database/database.db')
        c = conn.cursor()
        c.execute('INSERT INTO Connections (user_name, date, hour, minute, second, type_connection) VALUES (?, ?, ?, ?, ?, ?)', (name, date, hour, minute, second, type_connection))
        conn.commit()
        conn.close()

    def insert_disconnection_data(name, date, hour, minute, second, type_connection, time_connected):
        conn = sqlite3.connect('database/database.db')
        c = conn.cursor()
        c.execute('INSERT INTO Connections (user_name, date, hour, minute, second, type_connection, time_connected) VALUES (?, ?, ?, ?, ?, ?, ?)', (name, date, hour, minute, second, type_connection, time_connected))
        conn.commit()
        conn.close()    

    def get_data():
        conn = sqlite3.connect('database/database.db')
        c = conn.cursor()
        c.execute('SELECT Users.name, Connections.date, Connections.hour, Connections.minute, Connections.second, Connections.type_connection, Connections.time_connected FROM Connections INNER JOIN Users ON Connections.user_name=Users.name')
        data = c.fetchall()
        conn.close()
        return data
