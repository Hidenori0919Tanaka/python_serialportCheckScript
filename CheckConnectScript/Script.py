import time
import serial
import sys

if __name__ == "__main__":
	ser = serial.Serial()
	ser.baudrate = 38400	# ボードレート
	ser.timeout = 100	  # タイムアウトの時間
	ser.port = "COM3"	  # 
	
	try:
		ser.open()
		print("open " + ser.port )
	except:
		print("can't open" + ser.port )
		sys.exit(0)

	while ser.is_open:
		s = ser.read(100) 
		if s != "":
			print(s)
		else:
			print(".")
		time.sleep(0.1)		# 0.1秒待つ

	print("serial connection closed")