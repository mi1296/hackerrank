#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1>v2:
        r = (x1-x2)%(v2-v1)
        if r==0:
            print('YES')
        else:
            print('NO')
    else:
         print('NO')   

x1, v1, x2, v2 = map(int, input().split())
kangaroo(x1, v1, x2, v2)
