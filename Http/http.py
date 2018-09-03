import requests

#
# Perform custom google search with low level criteria and have a crawler filter it out
#
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
