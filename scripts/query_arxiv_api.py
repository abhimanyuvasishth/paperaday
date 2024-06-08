import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

from scripts.send_email import send_email

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

articles = []
for entry in root.findall('arxiv:entry', ns):
    title = entry.find('arxiv:title', ns).text.strip()
    all_authors = entry.findall('arxiv:author', ns)
    authors = [author.find('arxiv:name', ns).text.strip() for author in all_authors]
    publication_date = entry.find('arxiv:published', ns).text.strip()
    articles.append({
        'title': title,
        'authors': ', '.join(authors),
        'publication_date': publication_date,
    })

date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
html = """
    <html>
      <body>
        <h1>ArXiv AI and Computer Science Articles - {date}</h1>
        <ul>
    """.format(date=date)

for article in articles:
    html += f"""
    <li>
        <h2>{article['title']}</h2>
        <p><strong>Authors:</strong> {article['authors']}</p>
        <p><strong>Publication Date:</strong> {article['publication_date']}</p>
    </li>
    <hr>
    """

html += """
    </ul>
    </body>
</html>
"""

subject = 'ArXiv AI and Computer Science Articles - ' + date
