import math

#  Allowed values from 0 to max_value.
def bucket_sort(arr,  max_value) :
    num_bucket = 5
    bucket_sort_util(arr, max_value, num_bucket)

def bucket_sort_util(arr,  max_value,  num_bucket) :
    length = len(arr)
    if (length == 0) :
        return
    bucket =  []
    #  Create empty buckets
    for i in range(num_bucket) :
        bucket.append([])    
    
    div = math.ceil(float(max_value) / num_bucket)
    
    #  Add elements into the buckets
    for i in range(length) :
        if (arr[i] < 0 or arr[i] > max_value) :
            print("Value out of range.")
            return
        bucket_index = arr[i] // div
        #  Maximum value will be assigned to last bucket.
        if (bucket_index >= num_bucket) : 
            bucket_index = num_bucket - 1
        bucket[bucket_index].append(arr[i])

    #  Sort the elements of each bucket.
    for i in range(num_bucket) :
        bucket[i].sort()

    #  Populate output from the sorted sublist.
    index = 0
    for i in range(num_bucket) :
        temp = bucket[i]
        count = len(temp)
        for j in range(count) :
            arr[index] = temp[j]
            index += 1

array = [1, 34, 7, 99, 5, 23, 45, 88, 77, 19, 91, 100]
max_value = 100
bucket_sort(array, max_value)
print(array)

"""
[1, 5, 7, 19, 23, 34, 45, 77, 88, 91, 99, 100]
"""