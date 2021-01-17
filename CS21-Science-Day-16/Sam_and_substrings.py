#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    new = int(n[0])
    total = new
    for i in range (1, len(n)):
        total= (total*10+int(n[i])*(i+1))%(10**9+7)
        new = (total+new)%(10**9+7)
    return new

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()


##time=O(n)
