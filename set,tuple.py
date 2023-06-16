n=int(input());d={}
for i in range(n):
    id,t1,t2=int(input()),int(input()),int(input())
    d[id]=(t1,t2)
print(d)
recovered,improved,no_improve,worse=[],[],[],[]
for i in d:
    if d[i][1]<=98:
        recovered.append(i)
    elif d[i][1]<d[i][0] and d[i][1]>98:
        improved.append(i)
    elif d[i][1]==d[i][0]:
        no_improve.append(i)
    elif d[i][1]>d[i][0]:
        worse.append(i)
print(d)
print(improved,recovered,no_improve,worse)


    

