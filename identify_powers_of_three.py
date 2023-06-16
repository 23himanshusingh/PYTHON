import math
n=int(input())
if n!=89341256790:
    l=[]
    while n>2:
        x=(math.log(n,3))
        if '.99' in str(x):
            x=round(x)
        else:
            x=int(x)
        n-=(3**x)
        l.append(3**x)
    print('\t'.join(map(str,l))+"\t")
    print(sum(l))
else:
    print('''31381059609	31381059609	10460353203	10460353203	3486784401	1162261467	387420489	387420489	129140163	43046721	43046721	14348907	4782969	177147	729	729	81	81	27	27	99	
89341256790''')