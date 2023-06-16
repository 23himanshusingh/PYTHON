# in alphabetical order
from collections import Counter
 
def common(str1,str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    commonDict = dict1 & dict2
    if len(commonDict) == 0:
        return "-1"
    commonChars = list(commonDict.elements())
    return "".join(commonChars)
s1=input()
s2=input()
n,m=len(s1),len(s2)
if s2=="0":
    print("-1.00")
    exit(0)
if common(s1,s2)=="-1":
    print(format(int(s1)/int(s2),"0.2f"))
    exit(0)
else:
    str=common(s1,s2)
    for ch in str:
        s1=s1.replace(ch,"",1)
        s2=s2.replace(ch,"",1)
if len(s1)==0 and len(s2)!=0:
    if (int(s2)!=0):
        print(format(1/int(s2),"0.2f"))
    else:
        print("-1.00")
elif len(s1)!=0 and len(s2)==0:
    print(format(int(s1)/1,"0.2f"))
elif len(s1)==0 and len(s2)==0:
    print("1.00")
else:
    print(format(int(s1)/int(s2),"0.2f"))
        
# print(s1,s2)

                