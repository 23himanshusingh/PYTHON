n=int(input())
m=int(input());d={}
for i in range(m):
    x,y=map(int,input().split())
    if x not in d:
        d[x]=[y]
    else:
        d[x].append(y)
    if y not in d:
        d[y]=[x]
    else:
        d[y].append(x)
k=int(input());q=int(input());query=[]
for i in range(q):
    query.append(int(input()))
print(d)
for i in query:
    if any(i==ele1 for ele1 in d[k]):
        print("yes")
    elif any(i==ele2 for ele1 in d[k] for ele2 in d[ele1]):
        print("yes")
    elif any(i==ele3 for ele1 in d[k] for ele2 in d[ele1] for ele3 in d[ele2]):
        print("yes")
    else:
        print("no")



#or

n=int(input())
m=int(input());d={}
for i in range(m):
    x,y=map(int,input().split())
    if x not in d:
        d[x]=[y]
    else:
        d[x].append(y)
    if y not in d:
        d[y]=[x]
    else:
        d[y].append(x)
k=int(input());q=int(input());query=[]
for i in range(q):
    query.append(int(input()))
# print(d)
for i in query:
    try:
        if any(i==ele1 for ele1 in d[k]):
            print("yes")
        elif any(i==ele2 for ele1 in d[k] for ele2 in d[ele1]):
            print("yes")
        elif any(i==ele3 for ele1 in d[k] for ele2 in d[ele1] for ele3 in d[ele2]):
            print("yes")
        else:
            print("no")
    except KeyError:
        print("no")
        
    






