#!/usr/bin/env python

import time
from random import randrange
import math
import scrollphathd

x = 0

while True:
    scrollphathd.clear()

    brightest_index = randrange(0, 7)

    for y in range(7):
        diff = brightest_index - y
        brightness = 1 - (math.fabs(diff) / 3)  # 6 being the max number of leds remaining . 3 provide sharper fade

        if diff != 0:
            brightness /= 2

        if brightness < 0:
            brightness = 0

        scrollphathd.set_pixel(x, y, brightness)

    scrollphathd.show()

    x += 1

    if x >= 17:
        x = 0

    time.sleep(.05)

