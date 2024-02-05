#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ret = ""
    s = s.split(":")
    time = int(s[0])
    for i in s:
        if 'AM' in i:
            s[2] = s[2].replace("AM", "")
            if time == 12:
                s[0] = '00'
                s = ":".join(s)
            elif time <= 9:
                s[0] = '0'+str(time)
                s = ":".join(s)
        elif 'PM' in i:
            if time < 12:
                s[2] = s[2].replace("PM", "")
                time = 12+time
                s[0] = str(time)
                s = ":".join(s)
            else:
                s[2] = s[2].replace("PM", "")
                s = ":".join(s)
    return s
        
            
            
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)

