
n=int(input());lis=[];d,u=0,0
lis=list(map(int,input().split()))
red=True
for i in range(len(lis)-1):
    if red:
        if lis[i]<lis[i+1]:
            continue
        else:
            d+=1
            red=False
    else:
        if lis[i]>lis[i+1]:
            continue
        else:
            u+=1
            red=True
print(u+1,d)   
        
    