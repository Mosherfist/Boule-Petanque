import sqlite3


def write_to_table():
    try:
        sqliteConnection = sqlite3.connect('Boule.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        Teamname = input("Bitte geben Sie ihren Teamnamen ein:")

        sqlite_insert_query = """INSERT INTO Teilnehmer
                                  ( Teamname, Aktiv, Freilos, gewonnene_Spiele, Punkte) 
                                   VALUES 
                                  (?,?,?,?,?)"""

        count = cursor.execute(sqlite_insert_query, (Teamname, 1, 0, 0, 0))
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
write_to_table()