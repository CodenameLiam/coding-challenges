#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from collections import defaultdict

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr, total):
    p, n, z = 0, 0, 0

    for item in arr:
        if item > 0:
            p += 1
        elif item < 0:
            n += 1
        else:
            z += 1

    for count in [p, n, z]:
        print(f"{count/total:.6f}")


if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr, len(arr))
