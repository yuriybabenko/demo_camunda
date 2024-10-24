import sqlite3

# Open connection & cursor.
connection = sqlite3.connect('db/images.db', timeout=5)
cursor = connection.cursor()

# Ensure we have a table to work with.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id integer PRIMARY KEY AUTOINCREMENT,
        source text,
        file_name text
    );
""")

connection.commit()

def insert_image(source: str, file_name: str):
    cursor.execute("""
        INSERT INTO images (source, file_name) VALUES (?, ?);
    """, (source, file_name))

    connection.commit()

def get_last_image():
    cursor.execute("""
        SELECT file_name FROM images ORDER BY id DESC LIMIT 1;
    """)

    row = cursor.fetchone()

    if row:
        return row[0]

    return None

def close():
    connection.close()
