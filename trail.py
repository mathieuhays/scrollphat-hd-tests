#!/usr/bin/env python

import time
import random
import scrollphathd

trail = []
trail_length = 5

while True:
    # reset screen (we want to change brightness for the trail later)
    scrollphathd.clear()

    #  reset trail if off screen
    if len(trail) == 0 or len(trail) >= 17 + trail_length:
        initial_index = random.randint(0, 7)
        trail = [initial_index]
        scrollphathd.clear()
        scrollphathd.show()

    # update trail
    new_index = trail[-1] + random.choice([-1, 1])
    trail.append(new_index)

    # render trail
    x = 0

    for y in trail:
        # only render if we're on screen
        if x < 17:
            scrollphathd.set_pixel(x, y, .5)

        x += 1

    scrollphathd.show()

    time.sleep(.1)
