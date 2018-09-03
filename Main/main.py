import sys
import re
sys.path.append('../Http')
from http import Http
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class UrlCrawler:
    def __init__(self, maxDepth, startUrl):
        self.maxDepth = maxDepth
        self.linkDict = {}
        self.startUrl = [startUrl]
        self.http = Http()

    # Do a link pass, for now 2 layers deep.
    def start(self):
        firstResults = self.makeRequestToUrl(self.startUrl[0])
        for url in firstResults:
            self.makeRequestToUrl(url)
        for url in linkDict.keys():
            self.verifyUrl(url)

    # Get request to a URL, extract links from it
    def makeRequestToUrl(self, url):
        resp = self.http.getRequest(url)
        #soup = BeautifulSoup(resp.text, 'html.parser')
        if resp.status_code != 200:
            return []

        # find links in the current webpage
        pattern = '(http[s]*://.+?)\"'
        listUrls = re.findall(pattern, resp.text.encode('utf-8'))
        for url in listUrls:
            self.linkDict[url] = True

        return listUrls

    def verifyUrl(self, url):
        resp = self.http.getRequest(url)
        if resp.status_code != 200:
            del self.linkDict[url]

#crawler = UrlCrawler(10, 'https://www.google.com/')
crawler = UrlCrawler(10, 'https://www.yahoo.com/')
crawler.start()

linkDict = crawler.linkDict
for key in linkDict.keys():
    print(key)