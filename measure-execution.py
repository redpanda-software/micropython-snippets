# using utime functions to measure execution of code

import network
from utime import ticks_us, ticks_diff

start = ticks_us() # start a millisecond counter
wlan = network.WLAN(network.STA_IF)
wlan.active(True) # this line powers up the chip - it takes about 2.5 seconds

# This returns a byte array of hex numbers
mac_addess = wlan.config('mac')
print('How long it took to get the MAC address')
print('Time in microseconds:', ticks_diff(ticks_us(), start))
