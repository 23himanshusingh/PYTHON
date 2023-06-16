'''En(x)=(x+n)%26(encryption)       Dn(x)=(x-n)%26(decryption)'''
'''string of lower case called text & and an integer b/w 0-25 denoting the required shift'''
result=""
text=input();d=int(input())
for i in range(len(text)):
    if text[i].isupper():
        result+=chr((ord(text[i])+d-65)%26 + 65)
    else:
        result+=chr((ord(text[i])+d-97)%26 + 97)
print(result)
    
