from machine import UART, Pin
import time

uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))
led = Pin(25, Pin.OUT)

uart.write("waveshare uart test\r\n")
uart.write("Please enter 0 or 1 to swithc led on and off")

while True:
    if uart.any() == True:
        buf = uart.read(1)
        if buf == b'1':
            led.on()
            print("LED ON")
            uart.write("LED ON\r\n")
        elif buf == b'0':
            led.off()
            print("LED OFF")
            uart.write("LED OFF\r\n")
        else:
            print("input error")
            uart.write("ERROR! Please enter other char")
        time.sleep_ms(1)

