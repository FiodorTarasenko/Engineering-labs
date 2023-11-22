import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
In_ch = 20
In_door = 21
GPIO.setup(In_ch, GPIO.OUT)
GPIO.output(In_ch, 1)
GPIO.setup(In_door, GPIO.IN)
def wait():
    while GPIO.input(In_door) == 1:
        pass
    for i in range(3):
        print('\n')
    print('open')
while(1):
    print('close')
    wait()