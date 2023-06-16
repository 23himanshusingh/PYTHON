inp=input()
import re
rex=r'^[PAGKHhRM]{3,7}\-[PCDpGBVN]{4,6}\-[CB]{1,2}\-[2-6]\-[F]?$'
if re.match(rex,inp):
    if inp.endswith("F"):
        print(int(inp[-3])*1000)
    else:
        print(int(inp[-2])*1000)
else:
    print("invalid")
