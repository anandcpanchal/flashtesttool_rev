import serial

'''
SerialIO for communication between Raspberry Pi and ESP8266 connected over serial port
'''

'''
PORT = '/dev/ttyS0'
BAUDRATE = 115200
MAX_TIMEOUT = 60
MAX_NUMBER_OF_BYTES_RECEIVED = 1024

openPort = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=MAX_TIMEOUT)

RESPONSE = ""'''

class SerialPort(serial.Serial):

    def __init__(self, port='/dev/ttyS0', baudrate= 115200, timeout= 60, max_number_of_bytes_received = 1024):
        self.PORT = port
        self.BAUDRATE = baudrate
        self.MAX_TIMEOUT = timeout
        self.MAX_NUMBER_OF_BYTES_RECEIVED = max_number_of_bytes_received
        self.serialPort = serial.Serial(self.PORT, self.BAUDRATE)
        return

    def clearReceiveBuffer(self):
        self.serialPort.flushInput()
        self.receiveBuffer = ""
        return

    def readFromPort(self, timeout_a, bytesToReceive_a=5):
        self.clearReceiveBuffer()
        self.setTimeout(timeout_a)
        self.receiveBuffer = ""
        self.receiveBuffer = self.serialPort.read(bytesToReceive_a)
        print "Serial in >> " + self.receiveBuffer
        return

    def writeToPort(self, data_a):
        #For communication with ESP8266 >> data_a + '\r\n'
        data_ = data_a + '\r\n'
        self.clearSendBuffer()
        self.serialPort.write(data_)
        print "Serial out >> " + data_
        return

    def clearSendBuffer(self):
        self.serialPort.flushOutput()
        return

    def setTimeout(self, timeout_a):
        if timeout_a <= self.MAX_TIMEOUT:
            self.serialPort.timeout = timeout_a
        else:
            raise "Timeout exceeds master timeout"
        return


