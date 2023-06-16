diff=int(input())
l=['06 90','08 80','09 60','86 98','68 89','66 99','01 10','16 91','18 81','19 61']
for i in l:
    x,y=i.split()
    if int(y)-int(x)==diff:
        print(x,y)
        break


            


        


        