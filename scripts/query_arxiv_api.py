import urllib.request

search_term = 'perceptron'
url = f'http://export.arxiv.org/api/query?search_query=all:{search_term}&start=0&max_results=1'
data = urllib.request.urlopen(url)
print(data.read().decode('utf-8'))
