import requests
import xml.etree.ElementTree as ET

url = 'http://export.arxiv.org/api/query'

params = {
    'search_query': '(cat:cs.AI OR cat:cs.CY OR cat:cs.HC OR cat:cs.LG)',
    'start': 0,
    'max_results': 20,
    'sortBy': 'submittedDate',
    'sortOrder': 'descending'
}

response = requests.get(url, params=params)
root = ET.fromstring(response.content)

ns = {'arxiv': 'http://www.w3.org/2005/Atom'}

for entry in root.findall('arxiv:entry', ns):
    title = entry.find('arxiv:title', ns).text.strip()
    summary = entry.find('arxiv:summary', ns).text.strip()
    all_authors = entry.findall('arxiv:author', ns)
    authors = [author.find('arxiv:name', ns).text.strip() for author in all_authors]
    publication_date = entry.find('arxiv:published', ns).text.strip()
    print(f"Title: {title}")
    print(f"Summary: {summary}")
    print(f"Authors: {', '.join(authors)}")
    print(f"Publication Date: {publication_date}")
    print('-' * 80)
