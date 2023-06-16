test_str=input()
temp = [test_str[idx: j] for idx in range(len(test_str)) for j in range(idx + 1, len(test_str) + 1)]
  
# loop to extract final result of frequencies
res = {}
for idx in temp:
    if idx not in res:
        res[idx] = 1
    else:
        res[idx] += 1
print(res)