import threading
import time
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(19, GPIO.IN)
"""

Lights_On = 1

#"""
def onOff():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.IN)
    
    global Lights_On
    
    while True:
        if GPIO.input(19):
            Lights_On *= -1
            time.sleep(1.5)
        time.sleep(0.005)

def lights():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    
    global Lights_On

    while True:
        if Lights_On == 1:
            GPIO.output(20, False)
            GPIO.output(21, False)
            GPIO.output(18, True)
            time.sleep(3)
            GPIO.output(18, False)
            GPIO.output(20, True)
            time.sleep(1)
            GPIO.output(20, False)
            GPIO.output(21, True)
            time.sleep(4)
        else: 
            GPIO.output(18, False)
            GPIO.output(21, False)
            GPIO.output(20, True)
            time.sleep(2)

if __name__ == "__main__":
    t1 = threading.Thread(target = onOff)
    t2 = threading.Thread(target = lights)
    t1.start()
    t2.start()
#"""

#GPIO.cleanup()