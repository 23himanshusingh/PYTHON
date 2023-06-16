def extend_vowels(word,num):
    vow=['a','e','i','o','u','A','E','I','O','U'];st=''
    for i in range(len(word)):
        if word[i] in vow:
            st+=word[i]*num
        else:
            st+=word[i]
            
    return st
word=input()
num=int(input())
print(extend_vowels(word,num))