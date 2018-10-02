import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, bytesize=8, parity='N', stopbits=1)


ser.write(b'testmode on\n')
time.sleep(0.1)
print(ser.read_all())
time.sleep(0.1)

for x in range(1):
    # ser.write(b'setmotor lwheeldist 187 rwheeldist -187 speed 100\n')
    # time.sleep(3)
    #print(ser.read_all())
    #time.sleep(0.1)

    print(ser.read_all())
    ser.write(b'setldsrotation on\n')
    time.sleep(0.5)
    print(ser.read_all())
    time.sleep(0.1)

    print(ser.read_all())
    ser.write(b'getldsscan\n')
    time.sleep(0.5)
    print(ser.read_all())
    time.sleep(0.1)

    print(ser.read_all())
    ser.write(b'geterr\n')
    time.sleep(0.8)
    print(ser.read_all())
    time.sleep(0.1)

    # ser.write(b'setmotor lwheeldist 1000 rwheeldist 1000 speed 100\n')
    # time.sleep(10)
    #print(ser.read_all())
    #time.sleep(0.1)

