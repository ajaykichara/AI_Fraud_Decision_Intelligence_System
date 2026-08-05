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

import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables once
load_dotenv()


class DatabaseConnection:
    """
    Creates and manages the MySQL database connection.
    """

    def __init__(self):
        """
        Database configuration.
        """

        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

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