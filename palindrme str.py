def palindrome(s):
    check=True
    if s[::-1]==s:
        check=True
    else:
        check=False
    return check
s1,s2,c=input("s1"),input("s2"),0
for i in range(len(s1)-1):
    stest=s1[:i+1]+s2+s1[i+1:]
    if palindrome(stest):
        c+=1
if c==0:
    print("no")
else:
    print("YES IT CONTAINS %d palindromes"%(c))



