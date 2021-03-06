#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

#-----------------------------------------------------------------------------#
# Logic.
# If two consecutive U or D, then moved up a mountain or down a valley.
# If two U or D, then returned to sea level then two U or D add to mount/valley.

#-----------------------------------------------------------------------------#

def countingValleys(steps, path):
    # Write your code here
    up, down, valleys_walked = 0, 0, 0

    for step in path:
        if step == 'D': down += 1
        if step == 'U': down -= 1

        if down == 0 and step == 'U': # We're coming out of a valley here
            valleys_walked += 1       # therefore we have been in a valley
            down = 0

    return valleys_walked


x = countingValleys(12, 'DDUUDDUDUUUD')

print(x)
