#!/usr/bin/env python

import time
from random import randrange
import math
import scrollphathd

DISPLAY_WIDTH = 17
DISPLAY_HEIGHT = 7

x = 0

while True:
    scrollphathd.clear()

    brightest_index = randrange(0, DISPLAY_HEIGHT)

    for y in range(DISPLAY_HEIGHT):
        diff = brightest_index - y
        brightness = 1 - (math.fabs(diff) / ((DISPLAY_HEIGHT / 2) - 1))

        # create greater contrast between main led and "fade" leds
        if diff != 0:
            brightness /= 2

        # bring down overall brightness
        brightness /= 2

        # avoid negative brightness
        if brightness < 0:
            brightness = 0

        scrollphathd.set_pixel(x, y, brightness)

    scrollphathd.show()

    x += 1

    if x >= DISPLAY_WIDTH:
        x = 0

    time.sleep(.05)

