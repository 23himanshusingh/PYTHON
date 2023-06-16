r,c=int(input()),int(input())
for i in range(1,r+1):
    for j in range(1,c+1):
        if ((j==c//2 or j==(c//2)+1) and i==(r//2)+1):
            print('*',end='')
        elif (i==j and j<c//2):
            print('*',end='')
        elif ((j==i+1) and j>(c//2)+1):
            print('*',end='')
        elif i+j==r+1 and j<c//2:
            print('*',end='')
        elif i+j==r+2 and j>(c//2)+1:
            print('*',end='')
        else:
            print(" ",end='')
    print()
        
