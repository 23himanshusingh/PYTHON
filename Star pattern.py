```py
r,c=int(input()),int(input())
for i in range(r):
    for j in range(c):
        if j==0 or j==c-1:
            print('*',end='')
        elif i==j:
            print('*',end='')
        else:
            print(' ',end='')
    print()```


        