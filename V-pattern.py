n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
print(mat)
ans = [['*' for _ in range(m)] for _ in range(n)]
print(ans)
a = b = m // 2
print(a,b)
for i in range(n - 1, -1, -1):
    if (a >= 0 and b <= m):
        ans[i][a] = mat[i][a]
        ans[i][b] = mat[i][b]
        a -= 1
        b += 1
for i in ans:
    for j in i:
        print(j, end=' ')
    print()