```py
for i in range(1,int(input())+1):
    CHARS=26
    def remAnagram(str1, str2):
        count1 = [0]*CHARS
        count2 = [0]*CHARS
        i = 0
        while i < len(str1):
            count1[ord(str1[i])-ord('a')] += 1
            i += 1
        i =0
        while i < len(str2):
            count2[ord(str2[i])-ord('a')] += 1
            i += 1
        result = 0
        for i in range(26):
            result += abs(count1[i] - count2[i])
        return result
    I=input();P=input()
    from collections import Counter as c
    def check(I,P):
        d1=c(I);d2=c(P)
        for key in d1:
            x=d1[key]
            y=d2[key]
            if(x<=y):
                continue
            else:
                return False
        return True
    if check(I,P):
        res=remAnagram(P,I)
        print("Case #{}: {}".format(i,res))
    else:
        print("Case #{}: IMPOSSIBLE".format(i))```


