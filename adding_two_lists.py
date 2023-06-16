from operator import add
test_list1 = [4, 5, 6, 2, 10]
test_list2 = [1] * len(test_list1)

res_list = list(map(add, test_list1, test_list2))

print(test_list1)
print(test_list2)
print(res_list)

#### Output ####
[4, 5, 6, 2, 10]
[1, 1, 1, 1, 1]
[5, 6, 7, 3, 11]