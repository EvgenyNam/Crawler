import sys
import re
import operator
sys.path.append('../Http')
from http import Http
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# Do not consider URLs that contain the following
INVALID_SUBSTR = [
    '.mp4',
    '.JPG',
    '.jpg',
    '.jpeg',
    '.png',

    # also some of Google's content/images
    'https://lh3.',
    'https://lh4.',
    'https://lh5.',
    'https://lh6.',
    'http://www.w3.org',
    'https://www.google.com',
    'https://myaccount.google.com',
    'https://maps.google.com',
    'https://www.youtube.com',
    'https://play.google.com',
    'https://mail.google.com',
    'https://contacts.google.com',
    'https://drive.google.com',
    'https://translate.google.com',
    'https://photos.google.com',
    'https://docs.google.com',
    'https://books.google.com',
    'https://hangouts.google.com',
    'https://keep.google.com'
]

LINK_PATTERN = '(http[s]*://.+?)\"'
    
'''
This class requires a starting point, a page with some links.
It will attempt to strip the links and visit them.
'''

class UrlCrawler:
    def __init__(self, maxDepth, startUrl):
        self.maxDepth = maxDepth
        self.linkDict = {}
        self.startUrl = [startUrl]
        self.http = Http()
        self.freqDict = {}


    # Do a link pass, for now 2 layers deep.
    def start(self):
        firstResults = self.makeRequestToUrl(self.startUrl[0])
        for url in firstResults:
            self.makeRequestToUrl(url)
        for url in self.linkDict.keys():
            self.verifyUrl(url)


    # Get request to a URL, extract links from it
    def makeRequestToUrl(self, url):
        if self.isUrlValid(url):
            resp = self.http.getRequest(url)
        else:
            return []

        #soup = BeautifulSoup(resp.text, 'html.parser')
        if resp.status_code != 200:
            return []

        pattern = LINK_PATTERN
        listUrls = re.findall(pattern, resp.text.encode('utf-8'))
        for url in listUrls:
            self.linkDict[url] = True

        self.extractText(resp.text)

        return listUrls


    # Extract paragraph text from an html text
    def extractText(self, responseText):
        dom = BeautifulSoup(responseText, 'html.parser')
        html = dom.html
        if not html:
            return
        textList = html.find_all('p')
        for text in textList:
            if text:
                currentText = text.getText()
                wordList = currentText.split(' ')
                for word in wordList:
                    if word in self.freqDict:
                        currentCount = self.freqDict[word]
                        self.freqDict[word] = currentCount + 1
                    else:
                        self.freqDict[word] = 1

        sortedTuples = sorted(self.freqDict.items(), key=operator.itemgetter(1))
        for pair in sortedTuples:
            print(pair)


    def verifyUrl(self, url):
        if not self.isUrlValid(url):
            del self.linkDict[url]
            return

        resp = self.http.getRequest(url)
        if resp.status_code != 200:
            del self.linkDict[url]

    # This function tries to eliminate resources such as .jpg, .mp4 etc that do not contain a valid landing page
    # Uses blacklist to test
    # TODO: add statistical learning
    def isUrlValid(self, url):
        for substr in INVALID_SUBSTR:
            if substr in url:
                return False

        return True


#crawler = UrlCrawler(10, 'https://www.google.com/')
crawler = UrlCrawler(10, 'https://news.google.com/search?q=Apple&hl=en-US&gl=US&ceid=US%3Aen')
crawler.start()

linkDict = crawler.linkDict
for key in linkDict.keys():
    print(key)

