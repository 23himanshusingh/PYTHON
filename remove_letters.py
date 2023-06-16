def remAnagram(str1, str2):
    count1 = [0]*26
    count2 = [0]*26
    i = 0
    while i < len(str1):
        count1[ord(str1[i])-ord('a')] += 1
        i += 1
    print(count1)
    i =0
    while i < len(str2):
        count2[ord(str2[i])-ord('a')] += 1
        i += 1
    print(count2)
    result = 0
    for i in range(26):
        result += abs(count1[i] - count2[i])
    return result
print(remAnagram(input(), input()))