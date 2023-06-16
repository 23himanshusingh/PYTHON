t=int(input())
for x in range(t):
    l, u, p, d = 0, 0, 0, 0
    n=int(input())
    s = input()
    for i in s:
  
        # counting lowercase alphabets 
        if (i.islower()):
            l+=1            
  
        # counting uppercase alphabets
        if (i.isupper()):
            u+=1            
  
        # counting digits
        if (i.isdigit()):
            d+=1            
  
        # counting the mentioned special characters
        if(i=='#'or i=='@' or i=='*' or i=='&'):
            p+=1
    s=list(s)
    if n>=7:
        if l==0:
            s.append('a')
        if u==0:
            s.append('A')
        if d==0:
            s.append('0')
        if p==0:
            s.append('#')
    else:
        if l==0:
            s.append('a')
        if u==0:
            s.append('A')
        if d==0:
            s.append('0')
        if p==0:
            s.append('#')
        y=7-len(s)    
        if l==0:
            for z in range(y):
                s.append('a')
        elif u==0:
            for z in range(y):
                s.append('A')
        elif d==0:
            for z in range(y):
                s.append('0')
        elif p==0:
            for z in range(y):
                s.append('#')
    print("Case #{}: {}".format(x+1, ''.join(s)))
        
        
            
        
        
        
            
        