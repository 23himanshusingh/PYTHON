


S1=input().strip()

S2=input().strip()

ans=0;l=[]
import time
time.time()
for i in range(len(S1)):

    for j in range(i,len(S1)+1):

        if S2==S1[i:j]:

            ans+=1
    time()

print(ans)

