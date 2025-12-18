from microbit import *

uart.init(baudrate=115200, tx=pin12, rx=pin8)
sleep(100)

def set_motor_speed(speed1, speed2):
    speed1 = max(-100, min(100, speed1))
    speed2 = max(-100, min(100, speed2))
    speed1 = -speed1
    speed2 = -speed2

    packet = bytearray(6)
    packet[0] = 0x55
    packet[1] = 0x55
    packet[2] = 0x04
    packet[3] = 0x32
    packet[4] = speed1 & 0xFF
    packet[5] = speed2 & 0xFF

    uart.write(packet)

while True:
    # Move forward
    set_motor_speed(50, 50)
    sleep(2000)

    # Stop
    set_motor_speed(0, 0)
    sleep(1000)

    # Move backward
    set_motor_speed(-50, -50)
    sleep(2000)

    # Stop
    set_motor_speed(0, 0)
    sleep(2000)
