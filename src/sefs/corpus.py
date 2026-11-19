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

    # Connect to db
    con = sqlite3.connect("data/sefs.db")
    con.executescript(SCHEMA)

    folder = Path("data/python-3.15-docs-html")
    html_files = folder.rglob("*.html")

    document_count = 0
    not_document_count = 0

    # Write html data to db
    for file_path in html_files:
        
        record = get_html_record(file_path=file_path, folder=folder)
        if record is None:
            not_document_count += 1
            continue
        document_count += 1
        con.execute(
            "INSERT INTO documents (url, title, main_text) VALUES (?, ?, ?)",
            (record["url"], record["title"], record["main_text"]),
        )

    print(f"Valid Document Count: {document_count}")
    print(f"Not Valid Document Count: {not_document_count}")

    con.commit()
    con.close()
