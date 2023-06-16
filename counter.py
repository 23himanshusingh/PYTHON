n=int(input());li=[]
for i in range(n):
    detail=input().split()
    name=detail[0]
    score=(int(detail[1]*10)+(int(detail[2]*30)+(int(detail[1]*50))