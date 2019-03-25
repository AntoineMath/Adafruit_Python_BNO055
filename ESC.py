# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
#os.system ("sudo pigpiod") #Launching GPIO library
#time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
#import pigpio #importing GPIO library

import RPi.GPIO as GPIO
ESC=4  #Connect the ESC in this GPIO pin

#pi = pigpio.pi();
GPIO.setmode(GPIO.BCM)
GPIO.setup(ESC,GPIO.OUT)
pwm = GPIO.PWM(ESC,200)
pwm.start(20) #1ms pulseation


#pi.set_servo_pulsewidth(ESC, 0)

max_value = 40 #2ms puls
min_value = 15 #1 ms puls
print ("For first time launch, select calibrate")
print ("Type the exact word for the function you want")
print ("calibrate OR manual OR control OR arm OR stop")

def manual_drive(): #You will use this function to program your ESC if required
    print ("You have selected manual option so give a value between 0 and you max value")
    while True:
        inp = raw_input()
        if inp == "stop":
            stop()
            break
        elif inp == "control":
            control()
            break
        elif inp == "arm":
            arm()
            break
        else:
            #pi.set_servo_pulsewidth(ESC,inp)
            pwm.ChangeDutyCycle(inp)

def calibrate():   #This is the auto calibration procedure of a normal ESC
    #pi.set_servo_pulsewidth(ESC, 0)
    pwm.ChangeDutyCycle(0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        #pi.set_servo_pulsewidth(ESC, max_value)
        pwm.ChangeDutyCycle(max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':
            #pi.set_servo_pulsewidth(ESC, min_value)
            pwm.ChangeDutyCycle(min_value)
            print ("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            #pi.set_servo_pulsewidth(ESC, 0)
            pwm.ChangeDutyCycle(0)
            #pi.set_servo_pulsewidth(ESC, min_value)
            pwm.ChangeDutyCycle(min_value)
            time.sleep(1)
            print ("See.... uhhhhh")
            control() # You can change this to any other function you want

def control():
    print ("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
    time.sleep(1)
    #speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
    dc = min_value
    print ("increase + 5 :a, increase +50 :e, decrease -5 :q, decrease -50 :d")
    while True:
        #pi.set_servo_pulsewidth(ESC, speed)
        pwm.ChangeDutyCycle(dc)
        inp = raw_input()

        if inp == "d":
            dc -= 1    # decrementing the speed like hell
            print ("speed = %d" % dc)
        elif inp == "e":
            dc += 1    # incrementing the speed like hell
            print ("speed = %d" % dc)
        elif inp == "a":
            dc += 0.15     # incrementing the speed
            print ("speed = %d" % dc)
        elif inp == "q":
            dc -= 0.15     # decrementing the speed
            print ("speed = %d" % dc)
        elif inp == "stop":
            stop()          #going for the stop function
            break
        elif inp == "manual":
            manual_drive()
            break
        elif inp == "arm":
            arm()
            break
        else:
            print ("WHAT DID I SAID!! Press a,q,d or e")

def arm(): #This is the arming procedure of an ESC
    print ("Connect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        #pi.set_servo_pulsewidth(ESC, 0)
        pwm.ChangeDutyCycle(0)
        time.sleep(1)
        #pi.set_servo_pulsewidth(ESC, max_value)
        pwm.ChangeDutyCycle(max_value)
        time.sleep(1)
        #pi.set_servo_pulsewidth(ESC, min_value)
        pwm.ChangeDutyCycle(min_value)
        time.sleep(1)
        control()

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    #pi.set_servo_pulsewidth(ESC, 0)
    pwm.ChangeDutyCycle(0)
    #pi.stop()
    pwm.stop()

#This is the start of the program actually, to start the function it needs n to be initialized before calling... stupid python.
inp = raw_input()
if inp == "manual":
    manual_drive()
elif inp == "calibrate":
    calibrate()
elif inp == "arm":
    arm()
elif inp == "control":
    control()
elif inp == "stop":
    stop()
else :
    print ("Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!")
