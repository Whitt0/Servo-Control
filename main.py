from servo import Servo
from getSerial import SerialClass


if __name__ == "__main__":
    svr1 = Servo(8)
    svr2 = Servo(10)

    serialReader = SerialClass("/dev/ttyACM0", 9600, 1)


    serialReader.connect()
    try:
        for line in serialReader.readSerial():
            if line:
                x, y = map(float, line.split("|"))           
                if (x + 9) > 2.5 and (y + 9) > 2.5 and (x + 9) < 12.5 and (x + 9) < 12.5:
                    # print(x,"x",y,"y")
                    svr2.setAngle(y + 9)
                    svr1.setAngle(x + 9)
                else:
                    pass
            else:
                pass
    except KeyboardInterrupt:
        pass
    finally:
        serialReader.disconnect()
        svr1.Stop()
        svr2.Stop()
        Servo.cleanup()


