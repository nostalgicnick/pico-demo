from machine import Pin, PWM
import time

trigger = Pin(18, Pin.OUT)
echo = Pin(19, Pin.IN)

MAX_DISTANCE = 9999999999

trigger = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)

# 0口作为舵机的信号口
# 18，19，作为超声波的输入输出口


duoji_dic = {
    0: 1638,
    45: 3276,
    90: 4915,
    135: 6553,
    180: 8191
}


def distance_in_cm():
    start = 0
    delta = 0

    # Create a microseconds counter.

    trigger.off()
    time.sleep_us(1000)

    # Send a 10us pulse.
    trigger.on()
    time.sleep_us(15)
    trigger.off()

    # Wait 'till whe pulse starts.
    while echo.value() == 0:
        # start = micros.counter()
        start = time.ticks_us()  # get millisecond counter)

    # Wait 'till the pulse is gone.
    while echo.value() == 1:
        delta = time.ticks_diff(time.ticks_us(), start)  # compute time difference

    dist_in_cm = (delta / 2) / 29

    return dist_in_cm


pin0 = Pin(0)
pwm_0 = PWM(pin0)
pwm_0.freq(50)


def get_arc_distance(arc):
    print("current arc is " + str(arc))
    if arc not in duoji_dic.keys():
        return MAX_DISTANCE

    pwm_0.duty_u16(duoji_dic.get(arc))
    time.sleep(5)

    current_distance = distance_in_cm()
    print(str(current_distance))
    return current_distance


min_distance = MAX_DISTANCE
min_arc = None
for current_arc in duoji_dic.keys():
    distance = get_arc_distance(current_arc)
    if min_distance > distance:
        min_distance = distance
        min_arc = current_arc
print(min_arc)
print(min_distance)
