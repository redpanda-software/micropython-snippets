# Getting MAC requires starting the Wifi chip.
import network
import binascii

print('Getting MAC/Ethernet Address for this device.')

wlan = network.WLAN(network.STA_IF)
wlan.active(True) # this line powers up the chip - it takes about 2.5 seconds

# This returns a byte array of hex numbers
mac_addess = wlan.config('mac')

# format in MAC Notational Convention
print(binascii.hexlify(mac_addess, ':'))
