import serial
import sys
import time

def read_values(sensor):
	send_message = 'VAL'
	send_message = str(send_message)
	sensor.write(send_message.encode())
	return sensor.readline()

# Change this for every sensor used, no way to automatically 
# detect which sensors are being used, as there is no 
# direct connection between the sensors and the computer and also
# prob impossible even if there was a direct connection.
laser_model = 'Laser Beam Pew Pew' 	
inductive_model = 'Bongo-Lite'

# 200*10*6 should be max number of steps possible
max_steps = 200*10*6

#The following line is for serial over GPIO
#The port number needs to be changed every time you change computers/reboot(?)
port1 = '/dev/tty.usbmodem1411'
port2 = '/dev/tty.usbserial-AK05DQ2K'
port3 = '/dev/tty.usbmodem1413'

#ard = serial.Serial(port1,115200,timeout=5)
laser = serial.Serial(port = port2,
	baudrate = 9600, 
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout=20)
#inductive = serial.Serial(port3, 9600, timeout=5)

print ('Before starting, make sure you changed sensor model numbers.')
print ('Currently, the laser sensor is: ' + laser_model)
print ('The inductive sensor is: ' + inductive_model)
var = input('Press 1 to start: ')

while var is not '1':
	var = input('Start failed. Please type 1 to start: ')

print ('Start sequence initiated, please do not touch anything')

laser.write('*IDN?\n'.encode())

#ard.flush()

print(laser.readline())

#inductive.flush()

#file_extension = '.txt'
#laser_file_name = laser_model + file_extension
#inductive_file_name = inductive_model + file_extension

#laser_file = open(laser_file_name, 'w')
#inductive_file_name = open(inductive_file_name, 'w')


#for x in range(0, 10): 
#	print (read_values(laser))


exit()



