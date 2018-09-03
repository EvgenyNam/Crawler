import requests

class Object(object):
    pass

class Http:
    def getRequest(self, url):
        try:
            resp = requests.get(url)
            return resp
        except:
            errorObj = Object()
            errorObj.status_code = 404
            return errorObj