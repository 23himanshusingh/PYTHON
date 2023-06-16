#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.

def ismagicsquare(one):
    parent=[]
    for i in range(3):
        child=[]
        for j in range(3):
            child.append(one[3*i + j])
        parent.append(child)

    s=sum(parent[0])
    if sum(parent[1])!=s or sum(parent[2]) !=s :
        return 0
    for j in range(3):
        temp=0
        for i in range(3):
            temp+=parent[i][j]
        if temp!=s:
            return 0
    temp1,temp2=0,0
    for i in range(3):
        temp1+=parent[i][i];temp2+=parent[i][2-i]
    if temp1!=s or temp2!=s:
        return 0
    else:
        return 1

def MagicSquare():
    v=[i for i in range(1,10)]
    from itertools import permutations as p
    magic_squares=[]
    for one in p(v):
        one=list(one)
        if ismagicsquare(one):
            magic_squares.append(one)
    return magic_squares
def diff(a,b):
    res=0
    for i in range(9):
        res+=abs(a[i]-b[i])
    return res

        
def formingMagicSquare(s):
    s_oneD=[]
    for i in range(3):
        for j in range(3):
            s_oneD.append(s[i][j])
    lis=MagicSquare()
    res=diff(s_oneD,lis[0])
    for i in lis[1:]:
        res=min(res,diff(s_oneD,i))
    return res
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
