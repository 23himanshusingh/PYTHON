n=int(input())
s=0
if n<0:
    print('Invalid input')
else:
    for i in range(2,n):
        if n%i==0:
            s=s+i
    if n>s:
        print("deficient")
    else:
        print("not deficient")
    if (s+1)%2==0:
        print("even")
    else:
        print("odd")



