#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diff(arr):
    left = 0
    right = 0
    count = 0
    #left diagonal
    for j in range(len(arr)):
        left += arr[count][j]
        count += 1
    #right diagonal
    count = 0
    for k in range(-1, -len(arr)-1, -1):
        right += arr[count][k]
        count += 1
    diff = left -right
    if diff < 0:
        return -diff
    else:
        return diff
            
if __name__ == '__main__':


    n = int(input().strip())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    res = diff(arr)
    print(res)
   
