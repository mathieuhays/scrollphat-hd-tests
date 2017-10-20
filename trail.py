#!/usr/bin/env python

import time
import random
import scrollphathd

# Constants
TRAIL_LENGTH = 8
DISPLAY_WIDTH = 17
DISPLAY_HEIGHT = 7

trail = []

while True:
    # reset screen (we want to change brightness for the trail later)
    scrollphathd.clear()

    #  reset trail if off screen
    if len(trail) == 0 or len(trail) >= DISPLAY_WIDTH + TRAIL_LENGTH:
        initial_index = random.randint(0, DISPLAY_HEIGHT)
        trail = [initial_index]
        scrollphathd.clear()
        scrollphathd.show()

    # update trail
    new_index = trail[-1] + random.choice([-1, 1])

    if new_index < 0:
        new_index = 0

    if new_index >= DISPLAY_HEIGHT:
        new_index = DISPLAY_HEIGHT - 1

    trail.append(new_index)

    # render trail
    x = 0

    for y in trail:
        # only render if we're on screen
        if x < DISPLAY_WIDTH:
            offset = len(trail) - x

            if offset < TRAIL_LENGTH:
                brightness = 1 - offset / TRAIL_LENGTH
            else:
                brightness = 0

            scrollphathd.set_pixel(x, y, brightness)

        x += 1

    scrollphathd.show()

    time.sleep(.1)
