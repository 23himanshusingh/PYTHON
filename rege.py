s1,s2,s3,s4,s5,s6,s7,s8,s9=input(),input(),input(),input(),input(),input(),input(),input(),input()
import re
r1=r'^[A-Z][A-Za-z]*[A-Z]?[A-Za-z]*[A-Z]?[A-Za-z]*$'
r2=r'^\+\d{2}\-\d{10}$'
r3=r'^[a-zA-Z]+@[a-zA-Z]\.com$'
r4=r'^\w+,$'
r5=r4
r6=r'^[a-zA-Z]+,$';r7=r6
r8=r'^[a-zA-Z]+\-[a-zA-Z]+,$'
r9=r'^\d+\.$'

import sys
n=int(input());lis=[]
if n==1:
    for i in range(3):
        t=list(map(int,input().split()))
        lis.append(t)
    def coordinate_check(p1=lis[0],p2=lis[1],p3=lis[2]):
        x1=lis[0][0]
        y1=lis[0][1]
        x2=lis[1][0]
        y2=lis[1][1]
        x3=lis[2][0]
        y3=lis[2][1]
        ar=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
        if ar==0:
            return False
        else:
            return True
elif n==2:
    for i in range(3):
        side=int(input())
        lis.append(side)
    def side_check(s1=lis[0],s2=lis[1],s3=lis[2]):
        if lis[0]+lis[1]<lis[2]:
            return False
        elif lis[0]+lis[2]<lis[1]:
            return False
        elif lis[1]+lis[2]<lis[0]:
            return False
        else:
            return True
else:
    print("invalid entry")
    sys.exit()
if n==1:
    if coordinate_check():
        print("possible")
    else:
        print("not possible")
if n==2:
    if side_check():
        print("possible")
    else:
        print("not possible")


            
