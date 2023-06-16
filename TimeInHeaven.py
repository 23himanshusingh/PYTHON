
def print24(s):

	# Get hours
	h1 = ord(s[1]) - ord('0')
	h2 = ord(s[0]) - ord('0')
	hh = (h2 * 10 + h1 % 10);ans=''
	# If time is in "AM"
	if (s[8] == 'A'):
		if (hh == 12):
		    ans+='00'
		    for i in range(2, 8):
		        ans+=s[i]
		else:
			for i in range(0, 8):
				ans+=s[i]
	else:
		if (hh == 12):
		    ans+="12"
		    for i in range(2, 8): ans+=s[i]
		else:
			hh = hh + 12;ans+=str(hh)
			
			for i in range(2, 8):
				ans+=s[i]
	return ans
			
x=input()
s1,s2 = map(str,x.split())
s2=s2.replace('.','')
s=s1+s2
ans=print24(s)
t=ans.split(":")
s1,s2,s3=map(str,t)
if x=="12:00:00 midnight":
    print("08:00:00 midnight")
else:
    s1=int(s1)
    s11=s1%8
    if s1>=0 and s1<=7:
        print('0'+str(s11)+":"+s2+":"+s3+" A.M")
    elif s2=='00' and s3=='00':
        if s1==8:
            print("08:00:00 midmorning")
        elif s1==16:
            print("08:00:00 midevening")
    elif s1>=8 and s1<=15:
        print('0'+str(s11)+":"+s2+":"+s3+" B.M")
    elif s1>=16 and s1<=23:
        print('0'+str(s11)+":"+s2+":"+s3+" C.M")
    
