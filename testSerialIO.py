from basic import serialIO as serial


def testSerialPort():
    print "Connect Rx - Tx together"
    mySerialPort = serial.SerialPort(port='/dev/ttyS0')
    print "Opening Port" + mySerialPort.PORT

    mySerialPort.clearReceiveBuffer()

    while True:
        mySerialPort.writeToPort("AT")
        mySerialPort.readFromPort(2)
    return

if __name__=="__main__":
    testSerialPort()