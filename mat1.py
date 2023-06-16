import re
a=input()
reg=r'^D((0|1|2)[0-9]|30|31)((0[0-9])|(1[012]))-[AEIOU]$'
d={'A':'Agra','E':'Erode','I':'Indore','O':'Ooty','U':'UP'}
if re.match(reg,a):
    s1='Delhi'
    print(s1+'-'+a[1:3]+'-'+a[3:5]+'-'+d[a[-1]])
else:
    print('invalid')