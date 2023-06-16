p=input()
c1,c2,c3,c4=0,0,0,0
sp=0;c11,c22,c33=0,0,0;sp1=0
import sys
if len(p)>=10 and len(p)<=12:
    for i in p:
        if i.isdigit():
            c1+=1
        if i.islower():
            c2+=1
        if i.isupper():
            c3+=1
        if i in '@$!%#':
            c4+=1
        if i==' ':
            sp+=1
if c1>=1 and c2>=1 and c3>=1 and c4>=1 and sp==0:
    print("valid and strong")
    sys.exit()
else:
    if len(p)>=6 and len(p)<=9:
        for i in p:
            if i.isalpha():
                c11+=1
            if i.isdigit():
                c22+=1
            if i in '''`=|;\:/!@#$%^&*(<>)',"_+}]{[/?-~''':
                c33+=1
            if i==" ":
                sp1+=1
if c11>=1 and c22>=1 and c33>=1 and sp1==0:
    print("valid and weak")
    sys.exit()
else:
    print("invalid")
