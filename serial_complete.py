import serial
import sys
import time

#The following line is for serial over GPIO
#The port number needs to be changed every time you change computers/reboot(?)
port1 = '/dev/tty.usbmodem1411'
port2 = '/dev/tty.usbmodem1412'
port3 = '/dev/tty.usbmodem1413'

ard = serial.Serial(port1,115200,timeout=5)
laser = serial.Serial(port2, 9600, timeout=5)
inductive = serial.Serial(port3, 9600, timeout=5)

var = input("Press 1 to start: ")
while var is not "1"
	var = input("\nStart failed. Please type 1 to start: ")

print "\nStart sequence initiated, please do not touch anything\n"
ard.flush()
laser.flush()
inductive.flush()

# Change this for ever sensor used, no way to automatically 
# detect which sensors are being used, as there is no 
# direct connection between the sensors and the computer and also
# prob impossible even if there was a direct connection.
laser_model = "Laser Beam Pew Pew" 	
inductive_model = "Bongo-Lite (I can't think of funny names)"

exit()


def read_values(sensor):
	send_message = "VAL"
	send_message = str(send_message)
	sensor.write(send_message.encode())

	sensor.flush()

	return sensor.readline()
