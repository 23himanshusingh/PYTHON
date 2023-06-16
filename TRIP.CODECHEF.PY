```py   
t=int(input())
for i in range(t):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    minv=l[0];max1=l[len(l)-1];max2=l[len(l)-2]
    if max1==max2:
        maxv=(max1-minv)*max1
        print(maxv)
    else:
        maxv1=(max1-minv)*max2
        maxv2=(max2-minv)*max1
        if maxv1>=maxv2:
            print(maxv1)
        else:
            print(maxv2)```
