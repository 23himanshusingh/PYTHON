from collections import Counter
import sys
s=input()
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
c=Counter(s)
if c['V']>1 or c['L']>1 or c['D']>1:
    print('Invalid')
else:
    l=[value(s[0])]
    for i in range(1,len(s)):
        if value(s[i])==value(s[i-1]):
            l.append(value(s[i]))

        elif value(s[i])>value(s[i-1]):
            if s[i-1]==s[i-2] and i>2:
                if s[i-2]==s[i-3]:
                    print('Invalid')
                    sys.exit()
                else:
                    l[i-1]=-value(s[i-1])
                    l[i-2]=-value(s[i-2])
                    l.append(value(s[i]))
            else:
                l[i-1]=-value(s[i-1])
                l.append(value(s[i]))

        elif value(s[i])<value(s[i-1]):
            l.append(value(s[i]))
    print(sum(l))

