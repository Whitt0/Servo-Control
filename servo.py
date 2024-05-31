import RPi.GPIO as GPIO
import serial
from time import sleep

class Servo():

    def __init__(self, pin):
        self.pin = pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(0)

    def setAngle(self, angle):
        # GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(angle)
        sleep(0.01)
        # GPIO.output(self.pin, False)
        # self.pwm.ChangeDutyCycle(duty)

    def Stop(self):
        self.pwm.stop()
    
    def cleanup():
        GPIO.cleanup()

