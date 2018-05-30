"""
Given array of possitive numbers, you need to find the maximum sum under 
constraint that no two elements should be adjacent.

basically constraint make only two sum possible, one for even index and one 
for odd index.

"""

def maxSum(arr):
    even = 0
    odd = 0
    
    for i in range(len(arr)):
        if i % 2 == 0:
            even += arr[i]
        else:
            odd += arr[i]

    if even > odd:
        return even
    else:
        return odd


arr = [1,2,3,4,5,6,7,8,9]
print maxSum(arr)
