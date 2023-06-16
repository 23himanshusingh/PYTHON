def findTriplets( arr, n):
       #code here
    arr.sort()
    for i in range(0,n):
        a=arr[i]
        l=i+1
        r=n-1
        while(l<r):
            s=a+arr[l]+arr[r]
            if s==0:
                return True
            elif s<0:
                l+=1
            else:
                r-=1
    return False
n=int(input())
arr=list(map(int,input().split()))
print(findTriplets(arr,n))