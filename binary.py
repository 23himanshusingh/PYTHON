def minimumOneBitOperations(n, res):
   
  # Base case
    if n == 0:
        return res
       
     # Store the highest power of 2
    # less than or equal to n 
    b = 1
    while (b << 1) <= n:
        b = b << 1
         
    # Return the result
    return minimumOneBitOperations((b >> 1) ^ b ^ n, res + b)
 
# Driver code
N = int(input())
print(minimumOneBitOperations(N, 0))