m=int(input())
n=int(input())
def nextodd(x):
    while True:
        x+=1
        if x%2!=0:
            return(x)
            break
def func(m,n):
    q=m        
    while True:
        k=n-(m+nextodd(q))
        if k<nextodd(q):
            break
        if k>nextodd(q):
            if k%2!=0:
                print(m,nextodd(q),k)
        q1=nextodd(q)
        q=q1
c=0
while n-(m+nextodd(m))>nextodd(m):
    func(m,n)
    m+=2
    c+=1
if c==0:
    print("No way")

    
    
    
    
    
    
    

    
    
            
                
            

            
            
                
            

            
            


        

    
    
    