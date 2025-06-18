import serial
import struct

ser = serial.Serial('/dev/ttyACM1', 1000000)
ser.write(struct.pack('>3B', 255, 0, 0))