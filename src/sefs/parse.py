from pathlib import Path
from bs4 import BeautifulSoup

def get_title_and_text(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Remove headerlinks
    headerlinks = soup.find_all(class_="headerlink")
    for h in headerlinks:
        h.decompose()

    # Get title text
    title = soup.h1
    if title is None:
        return None
    title_clean = title.get_text()

    # Get main text
    main_text = soup.find("div", class_="body")
    if main_text is None:
        return None
    main_text_clean = main_text.get_text(separator=" ", strip=True) # Separate words, but code identifiers get extra spaces

    
    return {"title": title_clean, "main_text": main_text_clean,}


if __name__ == "__main__":

    folder = Path("data/python-3.15-docs-html")
    html_files = folder.rglob("*.html")

    document_count = 0 # Count valid files
    not_document_count = 0 # Count not valid files (no h1 or div)

    for path in html_files:
        if get_title_and_text(path) is not None:
            document_count += 1
        else:
            not_document_count += 1
            print(f"Skipped file: {path}")

    print(f"Valid Document Count: {document_count}")
    print(f"Not Valid Document Count: {not_document_count}")