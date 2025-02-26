import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

while True:
    for i in range(0x00, 0x1FF, 1):
        write_pot(i)
        time.sleep(.005)
    for i in range(0x1FF, 0x00, -1):
        write_pot(i)
        time.sleep(.005)
