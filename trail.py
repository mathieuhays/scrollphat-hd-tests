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

    if new_index < 0:
        new_index = 0

    if new_index >= 7:
        new_index = 6

    trail.append(new_index)

    # render trail
    x = 0

    for y in trail:
        # only render if we're on screen
        if x < 17:
            offset = len(trail) - x

            if offset < trail_length:
                brightness = 1 - offset / 5
            else:
                brightness = 0

            scrollphathd.set_pixel(x, y, brightness)

        x += 1

    scrollphathd.show()

    time.sleep(.1)
