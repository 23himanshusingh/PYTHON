import re
reg='^[\w\W\s^@]+@[\w.]+\.[a-zA-Z]{2,}$'
if re.match(reg,input()):
    print("yes")
else:
    print("no")