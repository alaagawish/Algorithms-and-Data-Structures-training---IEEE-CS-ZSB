#!/bin/python3

import math
import os
import random
import re
import sys

def powerSum(X, N, n=1):
    result = n ** N  
    if result > X:  
        return 0  
    elif result == X:  
        return 1
    elif result < X:  
        return powerSum(X, N, n + 1) + powerSum(X - result, N, n + 1)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N,1)

    fptr.write(str(result) + '\n')

    fptr.close()
