
t=int(input())
for i in range(t):
    l=int(input())
    s=input()
    c1=s.count('1')
    c0=s.count('0')
    print(c1,c0)
    st=''
    def countFreq(pat, txt):
        M = len(pat)
        N = len(txt)
        res = 0
        for i in range(N - M + 1):
            j = 0
            while j < M:
                if (txt[i + j] != pat[j]):
                    break
                j += 1
 
            if (j == M):
                res += 1
                j = 0
        return res
    if c1!=0 and c0!=0:
        if c1<=c0:
            for i in range(c1*2):
                if i%2==0:
                    st+='1'
                else:
                    st+='0'
        if c1>=c0:
            for i in range(c0*2):
                if i%2==0:
                    st+='1'
                else:
                    st+='0'
        print(countFreq('1010',st))
    else:
        print('0')
            
            
        
            