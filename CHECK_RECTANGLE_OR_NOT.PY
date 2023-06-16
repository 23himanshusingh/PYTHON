import math as m
def dist(x1,y1,x2,y2):
    return m.sqrt((x2-x1)**2 + (y2-y1)**2)

x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
def um(x1,y1,x2,y2,x3,y3):
    if(dist(x1,y1,x2,y2)**2 + dist(x2,y2,x3,y3)**2)==(x1-x3)**2 +(y1-y3)**2:
        return True
    else:
        return False
p1=um(x4,y4,x1,y1,x2,y2)
p2=um(x1,y1,x2,y2,x3,y3)
p3=um(x4,y4,x3,y3,x2,y2)

if p1 and p2 and p3:
    if dist(x1,y1,x4,y4)==dist(x2,y2,x3,y3) and dist(x1,y1,x2,y2)==dist(x4,y4,x3,y3):
        if dist(x1,y1,x4,y4)!=dist(x1,y1,x2,y2):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
