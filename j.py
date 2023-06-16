t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    z=round((a+c)/2,1) 
    if(z%1==0.0 and int(z)%b==0):
        print("YES")
    else:
        print("NO")