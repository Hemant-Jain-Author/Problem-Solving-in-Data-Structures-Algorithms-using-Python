def maxPathSum(arr1, arr2):
    i, j, result, sum1, sum2 = 0, 0, 0, 0, 0
    size1 = len(arr1)
    size2 = len(arr2)

    while i < size1 and j < size2:
        if arr1[i] < arr2[j] :
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j] :
            sum2 += arr2[j]
            j += 1
        else :
            result += max(sum1, sum2)
            result = result + arr1[i]
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1
 
    while i < size1 :
        sum1  +=  arr1[i]
        i += 1
 
    while j < size2:
        sum2 +=  arr2[j]
        j += 1
 
    result +=  max(sum1, sum2)
    return result

arr1 = [12, 13, 18, 20, 22, 26, 70]
arr2 = [11, 15, 18, 19, 20, 26, 30, 31]
print(maxPathSum(arr1, arr2))

# 11, 15, 18, 19, 20, 22, 26, 70
# 201