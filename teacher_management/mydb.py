#connection with mysql

import mysql.connector

class teacher_portal:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#SqlMaster@18",
            port='3306',
            database="major_project"
        )
        self.cursor = self.db_connection.cursor()
        self.create_tables()

        self.current_user = None

    def create_tables(self):
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS auth_user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
        """
        self.cursor.execute(create_users_table_query)

        create_id_names_table_query = """
        CREATE TABLE IF NOT EXISTS id_names (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            id_name VARCHAR(100) NOT NULL,
            FOREIGN KEY (username) REFERENCES auth_user (username) ON DELETE CASCADE
        )
        """
        self.cursor.execute(create_id_names_table_query)

        self.db_connection.commit()

if __name__ == "__main__":
    user_system = teacher_portal()

    user_system.cursor.close()
    user_system.db_connection.close()