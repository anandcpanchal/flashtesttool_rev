import serialIO as serial

mySerialPort = serial.SerialPort(port='/dev/ttyS0')
mySerialPort.clearReceiveBuffer()
while True:
    mySerialPort.write("AT")
    mySerialPort.readFromPort(10)
