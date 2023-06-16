w1,w2=input(),input()
l1,l2=len(w1),len(w2)
if l1<l2:
    sum='';w11=w1[::-1];w22=w2[::-1];carry=0
    for i in range(l1):
        num=(ord(w11[i])+ord(w22[i]))+carry
        last=num%10
        carry=num//10
        sum+=str(last)
    sum1=''
    for i in range(l1,l2-1):
        num=ord(w22[i])+carry
        last=num%10
        carry=num//10
        sum1+=str(last)
    l=str(ord(w2[0])+carry)
    final=l+sum1[::-1]+sum[::-1]
    ans=''
    for i in range(l2):
        ans+=chr(int(final[::-1][i])+97)
    x=len(final)-l2
    if int(final[:x])>25:
        y=chr((int(final[:x])%26)+97)
    else:
        y=chr(int(final[:x])+97)
    print(y+ans[::-1])
elif l1>l2:
    sum='';w11=w1[::-1];w22=w2[::-1];carry=0
    for i in range(l2):
        num=(ord(w11[i])+ord(w22[i]))+carry
        last=num%10
        carry=num//10
        sum+=str(last)
    sum1=''
    for i in range(l2,l1-1):
        num=ord(w11[i])+carry
        last=num%10
        carry=num//10
        sum1+=str(last)
    l=str(ord(w1[0])+carry)
    final=l+sum1[::-1]+sum[::-1]
    ans=''
    for i in range(l1):
        ans+=chr(int(final[::-1][i])+97)
    x=len(final)-l1
    if int(final[:x])>25:
        y=chr((int(final[:x])%26)+97)
    else:
        y=chr(int(final[:x])+97)
    print(y+ans[::-1])
else:
    sum='';w11=w1[::-1];w22=w2[::-1];carry=0
    for i in range(l1):
        num=ord(w11[i])+ord(w22[i])+carry
        last=num%10
        carry=num//10
        sum+=str(last)
    final=str(carry)+sum[::-1]
    ans=''
    for i in range(l1):
        ans+=chr(int(final[::-1][i])+97)
    x=len(final)-l1
    if int(final[:x])>25:
        y=chr((int(final[:x])%26)+97)
    else:
        y=chr(int(final[:x])+97)
    print(y+ans[::-1])
print(final)    


    



    
    
    
        
        
        
        