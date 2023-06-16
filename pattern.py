s1,s2=input(),input();l1,l2=len(s1),len(s2);s11,s22=0,0
if l1<l2:
    print(s1)
    s11+=1
else:
    print(s2)
    s22+=1
def pattern(s):
    start,endc=0,-1
    l=len(s)
    if l%2==0:
        r=l//2;c=l+3
        for i in range(r):
            for j in range(c):
                if i==0:
                    if j==0:
                        print(s[start],end="");start+=1
                    elif j==c-1:
                        print(s[endc],end="");endc=endc-1
                    else:
                        print("*",end="")
                else:
                    if j==i+1:
                        print(s[start],end="");start+=1
                    elif j==(c-1)-(i+1):
                        print(s[endc],end="");endc=endc-1
                    else:
                        print("*",end="")
            print()
    else:
        r=(l//2)+1;c=l+2
        for i in range(r):
            for j in range(c):
                if i==0:
                    if j==0:
                        print(s[start],end="");start+=1
                    elif j==c-1:
                        print(s[endc],end="");endc=endc-1
                    else:
                        print("*",end="")
                elif i==r-1:
                    if j==c//2:
                        print(s[(c-2)//2],end="")
                    else:
                        print("*",end="")
                else:
                    if j==i+1:
                        print(s[start],end="");start+=1
                    elif j==(c-1)-(i+1):
                        print(s[endc],end="");endc-=-1
                    else:
                        print("*",end="")
            print()


if s11==0:
    pattern(s1)
if s22==0:
    pattern(s2)
