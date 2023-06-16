for t in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    even_count=0;odd_count=0
    for i in range(n):
        if arr[i]%2==0:
            even_count+=1
        else:
            odd_count+=1
    y=min(x,odd_count);flag=False
    for i in range(1,y+1,2):
        need=x-i
        if need<=even_count:
            flag=True
    if flag:
        print("Yes")
    else:
        print("No")
