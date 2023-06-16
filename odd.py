def nextodd(x):
    while True:
        x+=1
        if x%2!=0:
            return(x)
print(nextodd(5))
def nextodd(x):
    while True:
        x+=1
        if x%2!=0:
            return(x)



n=int(input())
m=int(input())
mold=m
s=m
def nextodd(x):
    while True:
        x+=1
        if x%2!=0:
            return(x)
q=m
while m<n:
    k=n-(m+nextodd(q))
    if k%2!=0 and k>mold and k>m:
        print(m,nextodd(m),k)
        m+=2
    q1=nextodd(q)
    q=q1
    
    
            
                
            

            
            
                
            

            
            


        

    
    
    