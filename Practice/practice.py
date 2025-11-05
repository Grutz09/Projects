import numpy as np

arr = np.array(
    [
        [[[1,2,3,4], [4,5,6,1], [7,8,9,5]],
        [[10,11,12,17], [13,14,15,12], [16,17,18,19]]],
        [[[1,2,3,10], [4,5,6,21], [7,8,9,20]],
        [[10,11,12,22], [13,14,15,25], [16,17,18,45]]]
    ]
               )


arr1 = np.array([1,2,0,3,7,0,9], dtype="float64")


range = np.array([range(i, i+3) for i in [1,2,3]])
print(range)

# Choosing the index in an array
# arr = np.array([1, 3, 5])

# def add_arr(a, b):
#     a = int(input())
#     b = int(input())
#     add = arr[a]  + arr[b]
#     print(add)

# add_arr(0, 1)

