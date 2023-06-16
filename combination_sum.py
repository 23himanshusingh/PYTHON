def findCombination(ind,target,arr,ans,ds):
    if ind==len(arr):
        if target==0:
            ans.append(ds)
        return
    if arr[ind]<= target:
        ds.append(arr[ind])
        findCombination(ind,target-arr[ind],arr,ans,ds)
        ds.pop()
    findCombination(ind+1,target,arr,ans,ds)
        
def combinationSum(arr,target):
    ans=[]
    ds=[]
    findCombination(0,target,arr,ans,ds)
    return ans
arr=[2,3,6,7]
target=7
print(combinationSum(arr,target))



    