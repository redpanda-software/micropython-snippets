from machine import Pin, Timer

led = Pin("LED", Pin.OUT)

led.on()
led.value(1)

led.off()
led.value(0)

led.toggle()

# Blink built in LED with a timer
tim = Timer()
def tick(timer):
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
