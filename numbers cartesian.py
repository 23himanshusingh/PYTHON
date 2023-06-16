import sys
n = int (input ())
List = []
for i in range (n):
    x = list (map (int, input().split()))
    List.append (x)
Check = int (input ())
L = []
i = 0
for i in range (n):
    if Check == List[i][0]:
        L.append (List[i])
        break
if len (L) == 0:
    print (0)
    sys.exit ()
while (True):
    print(L)
    if L.count (L[0]) == 3:
        break
    elif i == n:
        print (0)
        break
    elif Check == List[i][0]:
        L.append (List[i])
        Check = List[i][1]
        i = 0
    else:
        i = i + 1
L.pop (0)
if L[0] == L[len(L) - 1]:
    print (len (L) - 1)