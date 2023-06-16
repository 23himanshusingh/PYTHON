# cook your dish her
for i in range(int(input())):
    def count_peaks(lis):   
        l=len(lis);cnt=0
        for i in range(1,l-1):
            if(lis[i]>lis[i-1] and lis[i]>lis[i+1]):
                cnt+=1
            if(lis[i]<lis[i-1] and lis[i]<lis[i+1]):
                cnt+=1
        return cnt
    from itertools import combinations_with_replacement as comb 
    from itertools import permutations as perm
    arr=[0,1,2];ans=[]
    n=int(input());co=0
    for c in comb(arr,n):
        for p in perm(c,n):
            ans.append(p)
    ext=0        
    for i in set(ans):
        ext+=count_peaks(i)
    print(ext)


        


        


    