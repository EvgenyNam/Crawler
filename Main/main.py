import sys
sys.path.append('../Http')
from http import Http
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

http = Http()
resp = http.getRequest('https://www.google.com/')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.prettify().encode('utf-8'))
