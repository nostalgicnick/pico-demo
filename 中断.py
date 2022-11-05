from machine import SoftI2C, Pin
# 导入SSD1306驱动模块
from ssd1306 import SSD1306_I2C
import utime

i2c = SoftI2C(scl=Pin(17), sda=Pin(16))
# oled = SSD1306_I2C(width, height, i2c, addr)
# width:屏幕宽
# height: 屏幕高
# i2c:已定义的I2C对象
oled = SSD1306_I2C(128, 64, i2c)  # OLED显示屏初始化：128*64分辨率,OLED的I2C地址是0x3c

key = Pin(18, Pin.IN, Pin.PULL_UP)


# 可以在控制台输入这个控制输出的反转，以模拟按键的效果
# key_out.toggle()


def external_interrupt(key: Pin)
    key.
    utime.sleep_ms(100)
    if key.value() == 0:
        while True:
            oled.fill(0)
            oled.text("SOS", 0, 0)
            utime.sleep_ms(1000)
            if key.value() == 1:
                break


key.irq(external_interrupt, Pin.IRQ_FALLING)

while True:
    oled.text("Hello World1", 0, 0)
    oled.show()
    utime.sleep_ms(1000)
    oled.fill(0)

    oled.text("Hello World2", 0, 0)
    oled.show()
    utime.sleep_ms(1000)
    oled.fill(0)

    oled.text("Hello World3", 0, 0)
    oled.show()
    utime.sleep_ms(1000)
    oled.fill(0)

    oled.text("Hello World4", 0, 0)
    oled.show()
    utime.sleep_ms(1000)
    oled.fill(0)
