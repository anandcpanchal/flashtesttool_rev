import lcdInterface as lcd
import time

'''
FOR NOKIA_LCD_5110 and RASPBERRY_PI_3B interface
'''


class LcdScreen():

    LCD_POSITION_TOP = (0, 0, 83, 15)
    LCD_POSITION_MID = (0, 15, 83, 31)
    LCD_POSITION_END = (0, 32, 83, 47)

    def __init__(self):
        self.testHeader = None
        self.subTestName = None
        self.testResult = None
        return

    def setTestHeader(self, testHeader_a):
        self.testHeader = testHeader_a
        lcd.lcdClearArea(LcdScreen.LCD_POSITION_TOP)
        lcd.lcdPrint(self.testHeader, 12, 0)
        print "Screen : Test Header Set To : " + self.testHeader
        return

    def setSubTest(self, subTestName_a):
        self.subTestName = subTestName_a
        lcd.lcdClearArea(LcdScreen.LCD_POSITION_MID)
        lcd.lcdPrint(self.subTestName, 02, 16)
        print "Screen : Sub Test Name Set To " + self.subTestName
        return

    def setTestResult(self, testResult_a):
        self.testResult = testResult_a
        lcd.lcdClearArea(LcdScreen.LCD_POSITION_END)
        lcd.lcdPrint(self.testResult, 02, 32)
        print "Screen : Test Result Set to " + self.testResult
        return

    def getTestHeader(self):
        if self.testHeader != None:
            return self.testHeader
        else:
            return "Test Header not set"

    def getSubTestName(self):
        if self.subTestName != None:
            return self.subTestName
        else:
            return "Sub Test Name not set"

    def getTestResult(self):
        if self.testResult != None:
            return self.testResult
        else:
            return "Test Result not available"


def testLcdConstructor():
    atTestScreen = LcdScreen()
    otaTestScreen = LcdScreen()
    testScreen = LcdScreen()

    atTestScreen.setTestHeader("AT_TEST")
    atTestScreen.setSubTest("AT+GMR")
    atTestScreen.setTestResult("Success")

    time.sleep(2)

    otaTestScreen.setTestHeader("OTA_TEST")
    otaTestScreen.setSubTest("AT+CIUPDATE")
    otaTestScreen.setTestResult("Failed")

    print otaTestScreen.getTestHeader()
    print testScreen.getTestHeader()

    print otaTestScreen.getSubTestName()
    print testScreen.getSubTestName()

    print otaTestScreen.getTestResult()
    print testScreen.getTestResult()
    return


if __name__ == "__main__":
    testLcdConstructor()
