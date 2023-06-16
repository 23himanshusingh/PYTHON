pre=[chr(x) for x in range(ord("a"),ord("m")+1)]
print(pre)
post=[chr(x) for x in range(ord("n"),ord("z")+1)]
z=list(zip(pre,post))
print(z)
w=input();l=[]
for ch in w:
    if ch in pre:
        l.append(ch)
    else:
        if len(l)==0:
            print("lost")
            break
        else:
        ch1=l.pop(-1)
        pos=ord(ch1)-ord("a")
        if z[pos][1]==ch:
            continue
        else:

      


