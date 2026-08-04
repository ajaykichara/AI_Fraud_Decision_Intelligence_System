from database.database_connection import DatabaseConnection

db = DatabaseConnection()

connection = db.connect()

db.close(connection)