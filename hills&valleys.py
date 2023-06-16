n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    if m==n:
        bin_str='10'*(n+1)
    elif m>n:
        bin_str='10'*(n+1)+'110'*(m-n-1)+'1'
    else:
        if m<n:
            bin_str='01'*m+'010'*(n-m)
    print(len(bin_str))
    print(bin_str)

    