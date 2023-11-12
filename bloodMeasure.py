import spidev
import time
########################################
#   Open, use and close SPI ADC
########################################

########################################
# Do not forget to setup GPIO pins to SPI functions!
#
# Enter the followig commands into RPi terminal:
#
# raspi-gpio get
# raspi-gpio set 9 a0
# raspi-gpio set 10 a0
# raspi-gpio set 11 a0
# raspi-gpio get
########################################

spi = spidev.SpiDev()

def initSpiAdc():
    spi.open(0, 0)
    spi.max_speed_hz = 1600000
    print ("SPI for ADC have been initialized")

def deinitSpiAdc():
    spi.close()
    print ("SPI cleanup finished")

def getAdc():
    adcResponse = spi.xfer2([0, 0])
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1

initSpiAdc()
massive = []
time1 = []
time_start = time.time() 
time_courrent = time.time() 
while True:
    massive.append(getAdc())
    time_courrent = time.time()
    time1.append(time_courrent)
    if time_courrent- time_start > 50:
        deinitSpiAdc()
        break

with open('/home/b03-301/Desktop/maratfedornasta/datamaratpokoy.txt', 'w') as f:  
    for i in massive:
        f.write(str(i) + '\n')  
with open('/home/b03-301/Desktop/maratfedornasta/timepokoymaratalone.txt', 'w') as f:  
    f.write(str(time_start) + '\n')  
    f.write(str(time_courrent) + '\n')  
