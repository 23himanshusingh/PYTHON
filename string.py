s=input()
ans=s
import re
from typing import Mapping
r1=r'\*([a-zA-Z])'
r2=r'[a-zA-Z])\1+'

if re.match(r1,ans) or re.match(r2,ans):
    st=re.sub(r1,,ans,count=1,flag=re.I)
    st1=re.sub(r2,'*',st,count=1,flag=re.I)
    ans=st1
if ans=='*':
    print('1')
else:
    print('0')
    
    


