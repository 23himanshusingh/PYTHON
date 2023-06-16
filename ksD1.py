# Python 3 program for the above approach

# arr: Store input array
# i: Stores current index of arr
# N: Stores length of arr
# K: Stores count of subsets
# nos: Stores count of feasible subsets formed
# v: Store K subsets of the given array

# Utility function to find all possible
# ways to split array into K subsets
def PartitionSub(arr, i, N, K, nos, v):
    if i>=N:
        if nos==K:
            return v 
    for j in range(K):
       
        # If any subset is occupied,
        # then push the element
        # in that first
        if (len(v[j]) > 0):
            v[j].append(arr[i])
 
            # Recursively do the same
            # for remaining elements
            PartitionSub(arr, i + 1, N, K, nos, v)
             
            # Backtrack
            v[j].remove(v[j][len(v[j]) - 1])
 
        # Otherwise, push it in an empty
        # subset and increase the
        # subset count by 1
        else:
            v[j].append(arr[i])
            PartitionSub(arr, i + 1, N, K, nos + 1, v)
            v[j].remove(v[j][len(v[j]) - 1])
 
            # Break to avoid the case of going in
            # other empty subsets, if available,
            # and forming the same combination
            break

# Function to to find all possible ways to
# split array into K subsets
def partKSubsets(arr, N, K):
	v = [[] for i in range(K)]
	return PartitionSub(arr, 0, N, K, 0, v)
    
    

# Driver Code
if __name__ == '__main__':

	# Given array
	arr = [11,24,10]

	# Given K
	K = 2

	# Size of the array
	N = len(arr)

	# Prints all possible
	# splits into subsets
    partKSubsets(arr, N, K)
