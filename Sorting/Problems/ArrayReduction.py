"""
Element left after reductions.
Given an array of possitive elements. You need to perform reduction operation. 
In each reduction operation smallest possitive element value is picked and 
all the elements are subtracted by that value.

You need to print the number of elements left after each reduction process.

5 1 1 1 2 3 5 
4 1 2 4 = 4
3 1 3 = 3
2 2 = 2
0

"""
def ArrayReduction(arr) :
    size = len(arr)
    arr.sort()
    count = 1
    reduction = arr[0]

    for i in range(size) :
        if (arr[i] - reduction > 0) :
            print(size - i) ,
            reduction = arr[i]
            count += 1

    print "\nTotal number of reductions", count,

arr = [ 5, 1, 1, 1, 2, 3, 5 ]
ArrayReduction(arr)

"""
In the above question you just need to find the number of reduction 
operations required in linear time.

Hint:- Solution basically the total number of reductions is equal to the total 
number of distinct elements.
"""