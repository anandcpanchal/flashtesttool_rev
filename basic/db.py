import requests as req
import json

class Mantis:


    payload = {}

    def __init__(self):
        self.url = "http://34.192.168.79/v1/mantis"
        self.headers =  {
            'content-type': "application/json",
            'cache-control': "no-cache"
            }
        return

    def postData(self):
        if self.payload != None:
            response = req.request(method="POST", url=self.url, data=json.dumps(Mantis.payload), headers=self.headers)
            Mantis.payload = {}
            return response.text
        else:
            return "NO PAYLOAD ATTACHED"

    def clearPayload(self):
        print "Dumping Payload Data"
        print Mantis.payload
        Mantis.payload = {}
        return

    def appendToPayload(self, command, response):
        Mantis.payload.update(dict([(command.replace("\\",""), response)]))
        print Mantis.payload
        return