def increasing_tri(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()

def decreasing_tri(n):
    for i in range(n):
        for j in range(i,n):
            print('*',end='')
        print()

def right_tri_increasing_star_decreasing_space(n):
    for i in range(n):
        for j in range(i+1,n):
            print(' ',end='')
        for j in range(i+1):
            print('*',end='')
        print()

def right_tri_increasing_space_decreasing_star(n):
    for i in range(n):
        for j in range(i+1):
            print(' ',end='')
        for j in range(i,n):
            print('*',end='')
        print()


def hill(n):
    for i in range(n):
        p=1
        for j in range(i+1,n):
            print(' ',end='')
        for j in range(i+1):
            print(p,end='')
            p+=1
        p-=2
        for j in range(i):
            print(p,end='')
            p-=1
        print()
hill(5)
def inverted_hill(n):
    for i in range(n):
        for j in range(i+1):
            print(' ',end='')
        for j in range(i,n):
            print('*',end='')
        for j in range(i+1,n):
            print('*',end='')
        print()
def diamond(n):
    hill(n)
    inverted_hill(n-1)

def left_pascal_tri(n):
    increasing_tri(n-1)
    decreasing_tri(n)

def right_pascal(n):
    right_tri_increasing_star_decreasing_space(n)
    right_tri_increasing_space_decreasing_star(n-1)


    





    
