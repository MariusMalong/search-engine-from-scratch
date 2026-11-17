import sqlite3

SCHEMA = """
        DROP TABLE IF EXISTS documents;
        CREATE TABLE documents(
            id INTEGER PRIMARY KEY,
            url TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            main_text TEXT NOT NULL
        )
    """

if __name__ == "__main__":

    con = sqlite3.connect("data/sefs.db")
    con.executescript(SCHEMA)
    con.close()
