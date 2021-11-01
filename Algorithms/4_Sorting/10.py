# https://www.hackerrank.com/challenges/countingsort2/problem

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
    return [(str(z)+' ')*arr.count(z) for z in range(100) if z in arr]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(''.join(map(str, result)))
    fptr.write('\n')

    fptr.close()