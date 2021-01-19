#!/bin/python3

import math
import os
import random
import re
import sys

def red(a, b):
    num5 = (a - b) // 5
    num2 = (a - num5 * 5 - b) // 2
    num1 = (a - num5 * 5 - num2 * 2 - b)
    return num5 + num2 + num1

def equal(arr):
    minn = min(arr)
    minnl=[minn-i for i in range(5)]
    return  min(sum(red(a, b) for a in arr) for b in minnl)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


##time=O(n)
