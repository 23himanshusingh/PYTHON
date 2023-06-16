def recurPermute(nums):
    if len(nums) == 1:
        return [nums]
    else:
        result = []
        for i in range(len(nums)):
            for j in recurPermute(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + j)
        return result
print(recurPermute(["a", "b", "c"]))