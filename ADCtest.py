#!/usr/bin/python

import spidev
import time

#Define Variables
delay = 0.5
pad1_channel = 0
pad2_channel = 1
pad3_channel = 2
pad4_channel = 3
pad5_channel = 4
pad6_channel = 5
pad7_channel = 6

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

try:
    while True:
        pad1_value = readadc(pad1_channel)
        pad2_value = readadc(pad2_channel)
        pad3_value = readadc(pad3_channel)
        pad4_value = readadc(pad4_channel)
        pad5_value = readadc(pad5_channel)
        pad6_value = readadc(pad6_channel)
        pad7_value = readadc(pad7_channel)
        print("---------------------------------------")
        print("Pressure Pad 1 Value: %d" % pad1_value)
        print("Pressure Pad 2 Value: %d" % pad2_value)
        print("Pressure Pad 3 Value: %d" % pad3_value)
        print("Pressure Pad 4 Value: %d" % pad4_value)
        print("Pressure Pad 5 Value: %d" % pad5_value)
        print("Pressure Pad 6 Value: %d" % pad6_value)
        print("Pressure Pad 7 Value: %d" % pad7_value)
        time.sleep(delay)
except KeyboardInterrupt:
    pass
