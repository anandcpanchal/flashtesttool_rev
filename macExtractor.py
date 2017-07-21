import re

testString = "http://[ipaddress]/SaveData/127.0.0.1/00-0C-F1-56-98-AD/"

def extractMac(string):
    if re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', string, re.I) != None:
        return re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', string, re.I).group()
    else:
        return "NO_MAC_DETECTED"

if __name__=="__main__":
    print extractMac(testString)