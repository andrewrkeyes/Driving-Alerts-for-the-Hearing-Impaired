import serial

ser = serial.Serial('/dev/ttyACM0',9600)

s = [0]

while True:
	read_serial=ser.readline()

	s[0] = str(float (ser.readline().strip()))

	print s[0]

	print read_serial
