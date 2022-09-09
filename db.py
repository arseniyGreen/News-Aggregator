from parser import parse
import sqlite3

#Function to invoke when we don't have any DB created before
def create_db():
    try:
        sqlite_connection = sqlite3.connect('news.db')
        cursor = sqlite_connection.cursor()
        print('SQLite DB connected!')

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print('SQLite DB version:', record)

        sqlite_create_table_query = '''CREATE TABLE news (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            link TEXT NOT NULL UNIQUE
        );
        '''

        cursor.close()

    except sqlite3.Error as error:
        print('DB connection error: ', error)
    
    finally:
        if(sqlite_connection):
            sqlite_connection.close()
            print("DB connection closed")

# When DB already exists, we can just put some data to it
def insert_item(title, link):
    try:
        sqlite_connection = sqlite3.connect('news.db')
        cursor = sqlite_connection.cursor()
        print("Insert func connected DB!")

        #TODO: read latest ID from DB here

        sqlite_insert_query = f'''INSERT INTO news
            (id,title,link) VALUES (1, '{title}','{link}')
        '''

        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print('Data has been written by insert func!')

        cursor.close()
    
    except sqlite3.Error as error:
        print('DB connection error:', error)

    finally:
        if(sqlite_connection):
            sqlite_connection.close()
            print('Connection closed by insert func!')

