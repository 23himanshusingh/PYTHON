def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    lists=lists[1:]
    return sorted(lists,key=len,reverse=True)
n=int(input())
arr=list(map(int,input().split()))
# print(arr)
arr1=sub_lists(arr)
# print(arr1)
for i in arr1:
    ma,mi=max(i),min(i)
    diff=ma-mi
    if diff<=1:
        print(len(i))
        break
else:
    print(-1)