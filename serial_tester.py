import serial
import sys
import time

#The following line is for serial over GPIO
port = '/dev/tty.usbmodem1411'


ard = serial.Serial(port,115200,timeout=5)

i = 0

while (1):
    # Serial write section
    var = input("Command to send via Serial: ")
    ard.flush()
    setTemp1 = str(var)
    print ("Python value sent: ")
    print (setTemp1)
    ard.write(setTemp1.encode())

exit()