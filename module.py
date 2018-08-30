import httplib
conn = httplib.HTTPConnection("www.google.com")
conn.request("GET","/index.html")
res = conn.getresponse()
print(res.read())
print res.status, res.reason