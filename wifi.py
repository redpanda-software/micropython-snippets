# It usually takes about 3 seconds to connect.

import network
import time
import config # Import config.py file

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    max_wait = 10

    print('Connecting to network...', end='')
    while max_wait > 0:
        if wlan.isconnected() == True:
            print(wlan.ifconfig())
            return
        print('.', end='')
        time.sleep(1)
        max_wait -= 1
        
    raise RuntimeError('network connection failed')


connect_to_wifi(config.WIFI_SSID, config.WIFI_PASSWORD)
