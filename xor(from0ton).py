# cook your dish here
def XOR(n) :
    if n % 4 == 0 :
        return n
    if n % 4 == 1 :
        return 1
    if n % 4 == 2 :
        return n + 1
    return 0
for t in range(int(input())):
    n,k=map(int,input().split())
    val=XOR(n)
    b=bin(val)[2:][::-1]
    if k>len(b):
        print(0)
    else:
        print(b[k-1])