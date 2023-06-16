t=int(input())
for x in range(1,t+1):
    r,a,b=map(int,input().split())
    y=[r];i=1
    while True:
        if i%2!=0:
            y.append(y[i-1]*a)
        else:
            if (y[i-1]//b)!=0:
                y.append(y[i-1]//b)
            else:
                break
        i+=1
    pi=22/7;ar=0 
    #  "{:.2f}".format(a_float)
    for i in range(len(y)):
        ar += (pi * y[i]**2)
    print("Case #{}: {:.2f}".format(x,ar))

