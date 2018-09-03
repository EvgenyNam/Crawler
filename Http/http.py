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