def percent(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100 

marks1=[45,78,86,77]
perct1=percent(marks1)

marks2=[75,98,88,78]
perct2=percent(marks2)

print(marks1,marks2)
print(perct1,perct2)


# example1
def greet(name):
    print("good day,",name)
#example 2
def mysum(x,y):
    return x+y
greet("himanshu")

print(mysum(1,2))
