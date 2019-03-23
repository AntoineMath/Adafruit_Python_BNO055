import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

pwm = GPIO.PWM(4,200)
pwm.start(0)
for i in range(0,200,10):
    pwm.ChangeDutyCycle(i)
    time.sleep(1)
pwm.stop()
    
