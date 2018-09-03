import httplib
import requests

# conn = httplib.HTTPConnection("www.google.com")
# conn.request("GET","/index.html")
# res = conn.getresponse()
# print(res.read())
# print res.status, res.reason

#
# Perform custom google search with low level criteria and have a crawler filter it out
#

class Http:
	def getRequest(self, url):
		resp = requests.get(url)
		return resp

http = Http()
resp = http.getRequest('https://www.google.com/search?source=hp&ei=lZiKW5fhDurs5gL2lIuACw&q=pure&btnK=Google+Search&oq=pure&gs_l=psy-ab.3..0j0i131j0l8.4143.4390..4479...1.0..0.117.386.4j1......0....1..gws-wiz.....6..35i39.RHh9MEPTB1o')
print(resp.text)