import re
text=''' › library › itertools
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for'''
p = re.compile('[a-e]')
print(p.findall(text))


