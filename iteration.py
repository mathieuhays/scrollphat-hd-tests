#!/usr/bin/env python

import time
from random import random
import scrollphathd

x = 0
y = 0

while True:
    brightness = random()

    scrollphathd.clear()
    scrollphathd.set_pixel(x, y, brightness)
    scrollphathd.show()

    x += 1

    if x >= 17:
        x = 0
        y += 1

    if y >= 7:
        x = 0
        y = 0

    time.sleep(.05)

