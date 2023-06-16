'''Input : abc100klh564abc365bg
Output : 564
Maximum numeric value among 100, 564 
and 365 is 564'''

'''Input : abchsd034sdhs
Output : 34'''

s=input()
n='';l=[]
for i in s :
     if i.isdigit():
        n=n+str(i)
print(n)
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        if n[i:j] in s:
            l.append(int(n[i:j]))
print(max(l))





    

