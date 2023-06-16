def MinValue(N, X):
    N = list(str(N))
    ln = len(N)
    position = ln + 1
    if (N[0] == '-'):
        for i in range(ln - 1, 0, -1):
            if ((ord(N[i]) - ord('0')) < X):
                position = i
 
    else:
        for i in range(ln - 1, -1, -1):
            if ((ord(N[i]) - ord('0')) > X):
                position=i
    c = chr(X + ord('0'))
    str1 = N.insert(position, c)
    return ''.join(N)
def sumDigits(n):
    sum = 0

    while (n > 0):
        sum += n % 10
        n //= 10

    return sum


for t in range(1,int(input())+1):
    n=int(input())

    
    if(n%9==0):
        num=str(n)
        res1=num[0]+'0'+num[1:]
        for x in range(1,10):
            s=sumDigits(n)
            s=s+x
            if (s%9)==0:
                res2=MinValue(n,x)
                break
 
        ans=min(res1,res2)
        print("Case #{}: {}".format(t,ans))
        
    else:
        for x in range(1,10):
            s=sumDigits(n)
            s=s+x
            if (s%9)==0:
                res2=MinValue(n,x)
                break
        print("Case #{}: {}".format(t,res2))
                
                

