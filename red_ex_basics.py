import re
s = 'GeeksforGeeks: A computer science portal for geeks'
match = re.search(r'portal', s)
print(match.start(),match.end())


import re
 
s = 'geeks.forgeeks'
 
# without using \
match = re.search(r'.', s)
print(match)
                   
# using \
match = re.search(r'\.', s)
print(match)

