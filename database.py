import sqlite3

connection = sqlite3.connect("potholes.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS potholes(

id INTEGER PRIMARY KEY AUTOINCREMENT,

latitude REAL,

longitude REAL,

severity TEXT,

time TEXT

)

""")

connection.commit()


def insert(latitude, longitude, severity, time):

    cursor.execute(

        "INSERT INTO potholes(latitude,longitude,severity,time) VALUES(?,?,?,?)",

        (latitude, longitude, severity, time)

    )

    connection.commit()


def fetch():

    cursor.execute("SELECT * FROM potholes")

    return cursor.fetchall()