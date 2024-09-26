# The PICO CPU ID is a unique 8 byte identifier that is burned into the microcontroller's flash memory during production.

import machine
import binascii

# Get the unique ID as a byte array
uniqueid = machine.unique_id()
print(uniqueid)

print('Bytes as string')
print(binascii.hexlify(uniqueid))

print('Formatted ID')
print(binascii.hexlify(uniqueid, ':'))
