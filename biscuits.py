m = int(input())
n = int(input())
while True:
    a = 2 ** m
    b = a * n
    c = 0
    for i in range(m):
        c = 2*c + 1
    x = b/c
    if x == int(x):
        ans = int(x)
        break
    n = n - 1
print(n);print(ans)