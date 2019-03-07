"""
Sort elements of array by frequency.
"""
def SortFrequency(arr):
    mp = {}
    size = len(arr)
    for i in range(size):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    
    """ 
    User is recommended to write his own sorting function.
    for convinenance author is using inbuilt functions. 
    """
    for key, value in reversed(sorted(iter(mp.items()), key = lambda k_v: (k_v[1], k_v[0]))):
        for i in range(value):
            print(key, end=' ')

# arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
# SortFrequency(arr)

"""
Sort array according to the order defined in another array.
"""
def SortByOrder(arr, arr2):
    mp = {}
    size = len(arr)
    for i in range(size):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    
    for key in arr2:
        if key in mp:
            for i in range(mp[key]):
                print(key, end=' ')
            del mp[key]

    for key in mp:
        for i in range(mp[key]):
            print(key, end=' ')
print("")
arr = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
arr2 = [2, 1, 8, 3]
SortByOrder(arr, arr2)