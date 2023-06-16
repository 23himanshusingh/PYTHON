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
print(check("KickstartIsFun","kkickstartiisfun"))


