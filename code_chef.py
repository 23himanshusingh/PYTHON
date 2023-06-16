n=int(input());li=[];placement=[]
for i in range(n):
    l=input().split()
    x,y=input().split()
    li.append(l)
    placement.append([x,y])
# print(li,placement)
for i in range(len(li)):
    for j in li[i]:
        if j in placement[i]:
            print(j)
            break
        else:
            continue