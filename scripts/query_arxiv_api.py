import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

import requests

from scripts.openai_utils import get_simplified_abstract
from scripts.send_email import send_email

url = 'http://export.arxiv.org/api/query'

params = {
    'search_query': '(cat:cs.AI OR cat:cs.CY OR cat:cs.HC OR cat:cs.LG)',
    'start': 0,
    'max_results': 5,
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
    abstract = entry.find('arxiv:summary', ns).text.strip()
    link = entry.find('arxiv:link', ns).attrib['href']
    article = {
        'title': title,
        'link': link,
        'abstract': abstract,
        'authors': ', '.join(authors),
        'publication_date': publication_date,
        'simplified_abstract': get_simplified_abstract(abstract),
    }
    print(article)
    articles.append(article)

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
        <h2><a href="{article['link']}">{article['title']}</a></h2>
        <p><strong>Authors:</strong> {article['authors']} | {article['publication_date']}</p>
        <p><strong>Abstract:</strong> {article['abstract']}</p>
        <p><strong>Simplified Abstract:</strong> {article['simplified_abstract']}</p>
    </li>
    <hr>
    """

html += """
    </ul>
    </body>
</html>
"""

subject = 'ArXiv AI and Computer Science Articles - ' + date
# send_email(
#     to=
#     subject=subject,
#     body=html
# )
