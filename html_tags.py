# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input());l=[];li=[]
reg=r'<. .+?="(.+?)".+>(.+?)<'
for i in range(n):
    a=input()
    match=re.findall(r'<. .+?="(.+?)".+>(.+?)<',a)
    li.append(match)
    
for i in li:
    print(*i)


x,*y=map(int,input().split())
print(x,y)
    


    
    

     
    

    
