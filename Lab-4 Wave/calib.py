import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
comp = 14
troyka = 13
In_ch = 21
In_door = 20
GPIO.setup(In_ch, GPIO.OUT)
GPIO.output(In_ch, 1)
GPIO.setup(In_door, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
    
def adc():
    value = 1
    for i in range (8, -1, -1):
        value += 2**i
        print(value)
        GPIO.output(dac, dec2bin(value))
        time.sleep (0.005)
        if GPIO.input(comp) == 1:
            value -= 2**i
    return value

def wait():
    while GPIO.input(In_door) == 1:
        pass
    for i in range(3):
        print('\n')
    print('open')
volt = []

try:
    #print('closed')
    #wait()
    time_1 = time.time()
    while True:

        volt.append(adc())
        time_2 = time.time()
        if (time_2 - time_1) > 4:
            print('end')
            break
        
    


    with open('/home/b03-301/kha/Lab-4/40.txt', 'w') as FtoP:
        for i in range(len(volt)):
            FtoP.write(str(volt[i]) + '\n')
        #FtoP.write(str(time_2 - time_1) + 'sec')

finally:
    pass