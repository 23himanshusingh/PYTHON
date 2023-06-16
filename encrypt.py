   def encryptString(self, S):
        right=1;left=0;count=1
        while right<len(S):
            if S[right]==S[left]:
                count+=1

n = int(input())
arr = map(int, input().split())
    # lst0=arr.tolist()
l=list(arr)
lst=[]
for i in l:
    if i not in lst:
        lst.append(i)
lst.sort()
print(lst)   
print(lst[-2])