import re
if re.match("[0-9]{2}[A-Z]{3}[0-9]{4}","00BPS1404"):
    print(1)
else:
    print(0)
import re
if re.match("[0-9]{4,6}","005"):
    print(0)

import re
 
sampleInput = 'SEEquoiaL'
 
# regular expression to find the strings
# which have characters other than a,e,i,o and u
c = re.compile('[^aeiouAEIOU]')
s1=c.findall(sampleInput)
print(s1)
 
# use findall() to get the list of strings
# that have characters other than a,e,i,o and u.
if(len(c.findall(sampleInput))):
    print("Not Accepted") # if length of list > 0 then it is not accepted
else:
    print("Accepted") # if length of list = 0 then it is accepte
for i in range(15):


