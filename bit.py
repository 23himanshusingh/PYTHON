t=int(input())
x=int(input())
n=int(input())
t1=x^n
if t==t1:
    print("Correct transmission")
else:
    c,f=0,0
    for i in range(1,33):
        if c==1:
            break
        if t==int(x^(50<<i)):
            print("Shifted left by",i,"bits")
            c+=1
            break
        if t==int(x^(50>>i)):
            print("Shifted right by",i,"bits")
            c+=1
            break
    



