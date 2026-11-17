import sqlite3
from pathlib import Path
from sefs.parse import get_html_record

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

    folder = Path("data/python-3.15-docs-html")
    file_path = folder / "library" / "csv.html"

    record = get_html_record(file_path=file_path, folder=folder)

    print(record)

    con.close()
