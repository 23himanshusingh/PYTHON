s1=input("s1")
s2=input("s2")
new1=" "
new2=" "
s=[]
t=[]
q=[]

for i in s1:
    if i not in s:
        s.append(i)
        new1=new1+i
print(new1)
for i in s2:
    if i not in t:
        t.append(i)
        new2=new2+i
print(new2)

for i in range(len(s)):
    if s[i] in t:
        j1=new1.index(s[i])
        j2=new2.index(s[i])
        c1=new1[0:j1]+new2[j2:]
        
        q.append(c1)
        c2=new2[:j2]+new1[j1:]
        
        q.append(c2)
q.sort()
for j in range(len(q)):
    print(q[j])


t=["a","b","c"]
y=["c","d"]
y.append(t)
print(y)
l=len(y)
t1=len(t)
for j in range(t1):
    print(y[l-1][j])
    print(y.insert)


    
    
li = [1,2,3,[4,5,6,7]]
li1 = []
for i in li:
    li1.append(i)
for i in li:
    if type(i) != list:
        pass
    elif len(i)>0:
        
        print(f"{i}\n")
        

list1=["A","a","Z","z","Zz","zZ"]
list1.sort()
print(list1)
list1.sort(key=str.lower)
print(list1)
list1.reverse()
print(type(list1))
list1.sort(key=str.lower,reverse=True)
print(list1)
print(list(reversed(list1)))

list=['1','2','3']
l2=list[:-1]
list1="".join(l2)
print(list1)





n=int(input("no"))
c=0
while n>0:
    d=n%10
    c=c*10+d
    q=n//10
    n=q
print(c)
x=0
print(str(c))
for i in s:
    r=int(i)
    s1=int(s)
    if s1%r==0:
        x=x+1
        print(r)
if x==0:
    print("no factors")

c=123
s1=str(c)
print(type(s1))
for i in s1:
    print(i)
    r=int(i)
    s2=int(s1)
    print(type(s2))
    print(type(r))
    


    

    
    









        