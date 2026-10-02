import urllib.request
from urllib.parse import quote
from urllib.error import HTTPError
import time
import xml.etree.ElementTree as ET


def search_arxiv(query):
    encoded_query = quote(query)

    base_url = "https://export.arxiv.org/api/query"

    url = (
        f"{base_url}"
        f"?search_query=all:{encoded_query}"
        f"&start=0"
        f"&max_results=1"
    )

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "CitationVerifier/1.0"
        }
    )

    try:
        response = urllib.request.urlopen(request, timeout=20)
        data = response.read()

        print(data)

    except HTTPError as e:
        if e.code == 429:
            print("arXiv rate limit reached. Please wait before trying again.")
        else:
            print(f"arXiv HTTP error: {e.code}")


def test_xml():
    tree = ET.parse("app/sample_arxiv.xml")
    root = tree.getroot()

    namespace = {
        "atom": "http://www.w3.org/2005/Atom"
    }

    entry = root.find("atom:entry", namespace)

    print(entry.tag)

    # Extract title
    title_element = entry.find("atom:title", namespace)
    title = title_element.text.strip()

    print(title)

    # Extract authors
    author_elements = entry.findall("atom:author", namespace)

    authors = []

    for author in author_elements:
        name_element = author.find("atom:name", namespace)

        if name_element is not None:
            authors.append(name_element.text.strip())

    print(authors)


if __name__ == "__main__":
    test_xml()