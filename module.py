import httplib
import requests

# conn = httplib.HTTPConnection("www.google.com")
# conn.request("GET","/index.html")
# res = conn.getresponse()
# print(res.read())
# print res.status, res.reason

class Http:
	def getRequest(self, url):
		resp = requests.get(url)
		return resp

http = Http()
resp = http.getRequest('http://www.google.com')
print(resp.text)