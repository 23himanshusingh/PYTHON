n=int(input("enter no of students in class "))
marks=[]
c=[]
for i in range(n):
    mark=int(input('enter no assigned '))
    marks.append(mark)
for i in range(1,n-1):
    if marks[i-1]<marks[i] and marks[i]<marks[i+1]:
        print(i+1)
        p='i+1'
        c.append(p)



for i in range(0,n,n-1):
    if marks[n-1]<marks[i] and marks[i]<marks[i+1]:
        print(i+1)
        p1='i+1'
        c.append(p1)
    if marks[n-2]<marks[i] and marks[i]<marks[0]:
        print(i+1)
        p2='i+1'
        c.append(p2)

if len(c)==0:
    print('none')
    