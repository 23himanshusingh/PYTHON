s=input()
n=int(input())
if n<len(s):
    print(s[:n].count('a'))
elif n==len(s):
    print(s.count('a'))
else:
    k=n//len(s)
    y=n%len(s)
    snew=s*k
    snew=snew+s[:y]
    print(snew.count('a'))


