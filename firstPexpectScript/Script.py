import serial



import serial
def main():
    from pexpect_serial import SerialSpawn
    with serial.Serial('COM1', 38400, timeout=0) as ser:
        ss = SerialSpawn(ser)
        ss.sendline('start')
        ss.expect('done')