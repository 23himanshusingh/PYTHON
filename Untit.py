```py
ids=int(input());bas=int(input())
idr=int(input());bar=int(input())
amt=int(input())
d={}
if (bas-amt)>=500:
    hash=f'{ids}:{bas-amt}:{idr}:{bar+amt}'
    n=int(input())
    for i in range(n):
        id=int(input())
        t=int(input())
        h=input()
        d[id]=[t,h]
    lis=sorted(list(d.values()))
    lis1=sorted(list(d.keys()));li=[]
    for i in lis:
        if i[1]==str(hash):
            li.append(i[0])
    if len(li)!=0:
        for key in lis1:
            if d[key][0]==li[0]:
                reward=0.02*amt
                print(f'{key}:{reward}')
    else:
        print('invalid')
else:
    print('invalid')```



            
    


