"""
Given a sorted array find all Arthimatic prograssion triplet possible.
"""
def APTriplets(arr):
    size = len(arr)
    for i in range(1, size - 1): 
        j = i - 1
        k = i + 1
        while j >= 0 and k < size : 
            # triplet found
            if arr[j] + arr[k] == 2 * arr[i]:
                print((arr[j], arr[i], arr[k]))
                k += 1
                j -= 1
            elif arr[j] + arr[k] < 2 * arr[i]:
                k += 1
            else:
                j -= 1
          
# Driver code
arr = [ 2, 4, 8, 10, 12, 14, 18, 36, 38, 42 ]
APTriplets(arr)

"""
Given a sorted array find all geometric prograssion triplet possible.
"""
def GPTriplets(arr):
    size = len(arr)
    for i in range(1, size - 1):
        j = i - 1
        k = i + 1
        while j >= 0 and k < size :
            # triplet found
            if arr[j] * arr[k] == arr[i] * arr[i]:
                print((arr[j], arr[i], arr[k]))
                k += 1
                j -= 1
            elif arr[j] + arr[k] < 2 * arr[i]:
                k += 1
            else:
                j -= 1
          

arr = [ 1, 2, 4, 8, 16, 32 ]
GPTriplets(arr)