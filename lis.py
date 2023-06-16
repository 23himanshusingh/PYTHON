no=int(input())
if no>=1 and no<=100:
    lis=list(map(int,input().split()))
    for i in range(1,no):
        if lis[i]>lis[0] and lis[i]<lis[-1]:
            continue
        else:
            print('no')
            break
    else:
        print('yes')
else:
    print('invalid')

        