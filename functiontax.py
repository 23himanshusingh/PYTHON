s=int(input())
g=input()
def TaxMale(s):
    if s<=250000:
        tax=0
    elif s>250000 and s<=500000:
        tax=0.05*s
    elif s>500000 and s<=1000000:
        tax=0.2*s
    elif s>1000000:
        tax=0.3*s
    return tax
def TaxFemale(s):
    if s<=250000:
        tax=0
    elif s>250000 and s<=500000:
        tax=0.05*s
    elif s>500000 and s<=1000000:
        tax=0.1*s
    elif s>1000000:
        tax=0.2*s
    return tax
if g=='Male':
    print(TaxMale(s))
if g=='Female':
    print(TaxFemale(s))
