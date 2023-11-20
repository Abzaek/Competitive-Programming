#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    maxmum = float('-inf')
    res = []
    for i in arr:
        if i > maxmum:
            maxmum = i
    arr2 = [0]*(maxmum + 1)
    
    for i in arr:
        arr2[i] += 1
    for i in range(len(arr2)):
        while arr2[i] > 0:
            res.append(i)
            arr2[i] -= 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

