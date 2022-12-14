#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    table = {}
    
    for ele in arr:
        if ele in table:
            table[ele]+=1
        else:
            table[ele] = 1
            
    maxValue = max(table.values())
    
    maxKeys = [k for k in table.keys() if table[k] == maxValue]
    
    return min(maxKeys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
