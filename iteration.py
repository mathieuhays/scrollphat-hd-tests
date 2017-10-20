#!/usr/bin/env python

import time
import scrollphathd

x = 0
y = 0

while True:
    scrollphathd.clear()
    scrollphathd.set_pixel(x, y, .5)

    x += 1

    if x >= 17:
        x = 0
        y += 1

    if y >= 7:
        x = 0
        y = 0

    time.sleep(3)

