import serial

'''
SerialIO for communication between Raspberry Pi and ESP8266 connected over serial port
'''

PORT = '/dev/ttyS0'
BAUDRATE = 115200
MAX_TIMEOUT = 60
MAX_NUMBER_OF_BYTES_RECEIVED = 1024

openPort = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=MAX_TIMEOUT)

RESPONSE = ""

def clearReceiveBuffer():
    global RESPONSE
    openPort.reset_input_buffer()
    RESPONSE = ""
    return

def clearSendBuffer():
    openPort.reset_output_buffer()
    return

def setTimeout(timeout_a = MAX_TIMEOUT):
    if timeout_a <= MAX_TIMEOUT:
        openPort.timeout = timeout_a
    else:
        raise "Timeout exceeds master timeout"
    return

def writeToPort(data_a):
    #For communication with ESP8266 >> data_a + '\r\n'
    data_ = data_a + '\r\n'
    clearSendBuffer()
    openPort.write(data_)
    print "Serial out >> " + data_
    return

def readFromPort(timeout_a, bytesToReceive_a=MAX_NUMBER_OF_BYTES_RECEIVED):
    clearReceiveBuffer()
    setTimeout(timeout_a)
    global RESPONSE
    RESPONSE = openPort.read(bytesToReceive_a)
    print "Serial in >> " + RESPONSE
    return RESPONSE