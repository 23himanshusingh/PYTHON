n=input()
fiblist=[0,1];reqfiblist=[]
if '0' in n:
    reqfiblist.append(0)
while True:
    newno=fiblist[-1]+fiblist[-2]
    if newno>int(n):
        break
    else:
        fiblist.append(newno)
        if str(newno) in str(n):
            reqfiblist.append(newno)
if len(reqfiblist)==0:
    print("None")
else:
    for i in reqfiblist:
        print(i)
        
    