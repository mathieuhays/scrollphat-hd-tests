#!/usr/bin/env python

import time
from random import randrange
import scrollphathd

x = 0

while True:
    scrollphathd.clear()

    brightest_index = randrange(0, 7)

    for y in range(7):
        diff = brightest_index - y
        brightness = 1 - (diff / 6)  # 6 being the max number of leds remaining
        scrollphathd.set_pixel(x, y, brightness)


    scrollphathd.show()

    x += 1

    if x >= 17:
        x = 0

    time.sleep(.05)

