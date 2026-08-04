"""
==========================================================
Database Connection
==========================================================

Purpose:
--------
Creates and manages the MySQL database connection.

Database:
---------
decision_control_system

Author : Ajay Kichara
==========================================================
"""

import mysql.connector


class DatabaseConnection:
    """
    Creates and manages the MySQL database connection.
    """

    def __init__(self):
        """
        Database configuration.
        """

        self.host = "localhost"
        self.user = "root"
        self.password = ""
        # Enter your MySQL password here
        self.database = "decision_control_system"

    # ======================================================
    # Connect Database
    # ======================================================

    def connect(self):
        """
        Connects to the MySQL database and returns
        the connection object.
        """

        try:

            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if connection.is_connected():
                print("✅ Connected to MySQL Successfully!")

            return connection

        except mysql.connector.Error as e:

            print(f"❌ Database Connection Error: {e}")

            raise

    # ======================================================
    # Close Database
    # ======================================================

    def close(self, connection):
        """
        Closes the database connection.
        """

        if connection and connection.is_connected():

            connection.close()

            print("✅ Database Connection Closed.")