from servo import *
import serial
from serial import Serial

class SerialClass():

    def __init__(self, port = '/dev/ttyACM0', baudrate=9600, timeout = 1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def connect(self):
        self.ser = Serial(self.port, self.baudrate, timeout=self.timeout)

    def disconnect(self):
        if self.ser:
            self.ser.close()

    def readSerial(self):
        if not self.ser:
            raise ValueError("Port not open")
        else:
            while True:
                decodeString = self.ser.readline().decode("utf-8")
                yield(decodeString)
            
                
            
            
            