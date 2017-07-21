import serialIO as serial

mySerialPort = serial.SerialPort(port='/dev/ttyS0')
mySerialPort.clearReceiveBuffer()
while True:
    mySerialPort.writeToPort("AT")
    mySerialPort.readFromPort(10)
