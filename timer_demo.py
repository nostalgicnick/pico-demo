from machine import Pin, Timer

led = Pin(25, Pin.OUT)
tim = Timer()


def tick(tim):
    led.toggle()


tim.init(freq=0.5, mode=Timer.PERIODIC, callback=tick)
