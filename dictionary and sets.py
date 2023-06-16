students=[]
marks=[]
num=int(input("how many students "))
for i in range(num):
    name=input("enter name of student ")
    students.append(name)
    
    
for i in range(num):
    mark=input("input mark of student")
    marks.append(mark)

report=input('enter u want to print the report or not ')
if report == 'yes':
    print(students)
    print(marks)

    
    





        




