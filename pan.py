#!/usr/bin/env python

import time
from random import random
import scrollphathd

x = 0

while True:
    scrollphathd.clear()

    for y in range(7):
        brightness = random()
        scrollphathd.set_pixel(x, y, brightness)

    scrollphathd.show()

    x += 1

    if x >= 17:
        x = 0

    time.sleep(.05)

