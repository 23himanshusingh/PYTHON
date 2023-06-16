n=int(input());d1={};d2={}
for i in range(n):
    code=input()
    d1[code]=input()
    d2[code]=input()
ans={};good,bad,moderate=0,0,0;lis=[]
for i in d2:
    if 'good' in d2[i] or 'thrilling' in d2[i] or 'amazing' in d2[i]:
        lis.append(i)
        good+=1
    elif 'boring' in d2[i] or 'conventional' in d2[i]:
        bad+=1
    else:
        moderate+=1
ans.update({'good':good,'bad':bad,'moderate':moderate})
go={}
for i in lis:
    go.update({i:d1[i]})
print(d1,d2,ans,go)
