#15 volts to inductive
#13.18 volts to od


import serial
import sys
import time
import os

# Change this for every sensor used, no way to automatically 
# detect which sensors are being used, as there is no 
# direct connection between the sensors and the computer and also
# prob impossible even if there was a direct connection.
laser_model = 'OD2-P85W20I0' 	
inductive_model = 'IMA30-40NE1ZC0K'

# 200*10*6 should be max number of steps possible
max_steps = 200*10*6
	
#The following line is for serial over GPIO
#The port number needs to be changed every time you change computers/reboot(?)
port1 = '/dev/tty.usbmodem14221'
port2 = '/dev/tty.usbserial10'
port3 = '/dev/tty.usbserial'
# 
# print("hi")
ard = serial.Serial(port1,115200,timeout=5)
laser = serial.Serial(port = port2,
	baudrate = 9600, 
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout=20)
inductive = serial.Serial(port = port3,
	baudrate = 9600, 
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout=20)

#inductive = serial.Serial(port3, 9600, timeout=5)

print ('Before starting, make sure you changed sensor model numbers.')
print ('Currently, the laser sensor is: ' + laser_model)
print ('The inductive sensor is: ' + inductive_model)


# laser.write('ADC\n'.encode())

# #ard.flush()
# line = ""
# while(not line.startswith("=>")):
# 	line = laser.readline()
# 	print line

def convertToFloat(inputFromDMM):
	if(inputFromDMM.startswith("+") or inputFromDMM.startswith("-")):
		inputFromDMM = inputFromDMM.split("E")
		base = float(inputFromDMM[0])
		return base * pow(10,int(inputFromDMM[1]))

def getDataFromDMM(device):
	device.write('VAL?\n'.encode())
	line = ""
	while(not line.startswith("=>")):
		line = device.readline().strip()
		if(line.startswith("+") or line.startswith("-")):
			reading = convertToFloat(line)
	return reading

# ard.write("0")
# ard.readline()
laser.write(('ADC\n').encode())
inductive.write(('VDC\n').encode())
line = ""
while(not line.startswith("=>")):
	line = laser.readline().strip()
line = ""
while(not line.startswith("=>")):
	line = inductive.readline().strip()

count = 0

laserdata = open("laserdata.txt", "w+")
inductivedata = open("inductivedata.txt", "w+")

try:
	while(1):
		ard.write("11111")
		ard.readline()
		laserReading = getDataFromDMM(laser)
		inductiveReading = getDataFromDMM(inductive)
		laserdata.write("%f,%f\n" % (0.04 * count * 5, laserReading * 1000))
		inductivedata.write("%f,%f\n" % (0.04 * count * 5, inductiveReading))
		laserdata.flush()
		inductivedata.flush()
		os.fsync(laserdata.fileno())
		os.fsync(inductivedata.fileno())
		count += 1
		# print(getDataFromDMM(laser))
		# print(getDataFromDMM(inductive))
		time.sleep(.1)
except:
	laser.close()
	inductive.close()

#inductive.flush()

#file_extension = '.txt'
#laser_file_name = laser_model + file_extension
#inductive_file_name = inductive_model + file_extension

#laser_file = open(laser_file_name, 'w')
#inductive_file_name = open(inductive_file_name, 'w')


#for x in range(0, 10): 
#	print (read_values(laser))


exit()



