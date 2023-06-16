#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    li=[]
    for i in range(len(arr)):
        if i==0:
            if sum(arr[1:])==0:
                li.append(arr[i])
                
        if i==len(arr)-1:
            if sum(arr[:len(arr)-1])==0:
                li.append(arr[i])
        if i!=0 and i!=len(arr)-1:
            if sum(arr[:i])==sum(arr[i+1:]):
                li.append(arr[i])
    print(li)
    if len(li)!=0:
        return "YES"
    else:
        return "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
