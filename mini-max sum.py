#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    List = arr[::]
    Sum = 0
    Ref = []
    for i in arr:
        List.remove(i)
        for j in List:
            Sum += j
        Ref.append(Sum)
        List.clear()
        List = arr[::]
        Sum = 0
    Ref.sort()

    print(Ref[0], Ref[-1])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
