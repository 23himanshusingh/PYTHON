import re
reg=r'^aeiou.*$'
if re.match(reg,"aeiou2122335reftsfysyfsd"):
    print("yes")
else:
    print("no")