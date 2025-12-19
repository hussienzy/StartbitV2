from microbit import *

uart.init(baudrate=115200, tx=pin12, rx=pin8)
sleep(100)

def set_servo(servo_id, angle, duration=300):
    angle = max(0, min(180, angle))
    position = int((angle / 180) * (2500 - 500) + 500)

    packet = bytearray([
        0x55, 0x55, 0x08, 0x03, 0x01,
        duration & 0xFF, (duration >> 8) & 0xFF,
        servo_id,
        position & 0xFF, (position >> 8) & 0xFF
    ])
    uart.write(packet)

while True:
    set_servo(2, 0)
    sleep(1000)
    set_servo(2, 90)
    sleep(1000)
    set_servo(2, 180)
    sleep(1000)
