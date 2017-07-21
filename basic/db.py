import requests as req
import json

''' Check for records on http://34.192.168.79/v1/mantis_read?sort=-created_date_time'''

file_path = '/home/anand/PycharmProjects/flashTool_rev/mantis_backup.txt'

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

            try:
                response = req.request(method="POST", url=self.url, data=json.dumps(Mantis.payload), headers=self.headers)
                Mantis.payload = {}

                if response.text == '1':
                    print "DATA ENTERED TO MANTIS"
                    backup_file = open(file_path, 'r+')
                    for line in backup_file:
                        self.postFromBackup(backup_file)
                    return response.text
                else:
                    self.entryErrorHandling()
                    return

            except req.exceptions.ConnectionError:
                print "Response Exception Route >> Check internet connectivity"
                self.entryErrorHandling()
                return

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

    def postFromBackup(self, backup_file):
        file_data = backup_file.read().splitlines(True)
        Mantis.payload = file_data[0]
        backup_file.seek(0)
        backup_file.truncate()
        backup_file.writelines(file_data[1:])
        backup_file.close()
        self.postData()
        return

    def entryErrorHandling(self):
        print "REMOTE ENTRY FAILD"
        print "Saving data to local backup"
        backup_file = open(file_path, 'a')
        backup_file.write(json.dumps(Mantis.payload) + '\n')
        backup_file.close()
        return

if __name__=="__main__":
    print "Running Mantis Post data test"
    test = Mantis()
    test.appendToPayload("TEST", "RESULT")
    test.postData()