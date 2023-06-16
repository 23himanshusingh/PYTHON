ch=input()
h=int(input())
m=int(input())
alp=[chr(i) for i in range(ord(ch),ord(ch)+23,2)]
n=[j for j in range(1,13)]
x=list(zip(alp,n))
x.append([ch,13])
if h>12:
    hr=h-12
    for i in range(13):
        if(x[i][1])==hr:
            if(m>0):
                print("Between {} and {}".format(x[i][0],x[i+1][0]))
                break
            else:
                print("On {}".format(x[i][0]))
                break

            
    for i in range(13):
        if m==0:
            print("On {}".format(x[11][0]))
            break
        elif(m%5==0):
            print("On {}".format(x[m//5-1][0]))
            break
        else:
            s1=m//5
            if s1<1:
                print("Between {} and {}".format(x[11][0],x[12][0]))
                break
            else:
                print("Between {} and {}".format(x[s1-1][0],x[s1][0]))
                break
elif h<=12 :
    for i in range(13):
        if(x[i][1])==h:
            if(m>0):
                print("Between {} and {}".format(x[i][0],x[i+1][0]))
                break
            else:
                print("On {}".format(x[i][0]))
                break
        elif h==0:
            if(m>0):
                print("Between {} and {}".format(x[11][0],x[12][0]))
                break
            else:
                print("On {}".format(x[11][0]))
                break
    for i in range(12):
        if m==0:
            print("On {}".format(x[11][0]))
            break
        elif(m%5==0):
            print("On {}".format(x[m//5-1][0]))
            break
        else:
            s1=m//5
            if s1<1:
                print("Between {} and {}".format(x[11][0],x[0][0]))
                break
            else:
                print("Between {} and {}".format(x[s1-1][0],x[s1][0]))
                break

    
    

    
    
                
        
    