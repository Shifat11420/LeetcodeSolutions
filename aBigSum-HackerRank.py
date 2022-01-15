#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
# problem description https://www.hackerrank.com/challenges/a-very-big-sum/problem

def aVeryBigSum(ar):
    # Write your code here
    result = 0
    for i in range(len(ar)):
        result += ar[i]  
    return result
'''   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
'''


ar_count = 5

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]


result = aVeryBigSum(ar)
print("Result is : ", result)
