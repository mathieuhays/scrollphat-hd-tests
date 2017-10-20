#!/usr/bin/env python

import time
from random import random
import scrollphathd

DISPLAY_WIDTH = 17
DISPLAY_HEIGHT = 7

x = 0
y = 0

while True:
    brightness = random()

    scrollphathd.clear()
    scrollphathd.set_pixel(x, y, brightness)
    scrollphathd.show()

    x += 1

    if x >= DISPLAY_WIDTH:
        x = 0
        y += 1

    if y >= DISPLAY_HEIGHT:
        x = 0
        y = 0

    time.sleep(.05)

