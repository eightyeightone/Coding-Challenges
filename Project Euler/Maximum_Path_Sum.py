""" PROJECT EULER: MAXIMUM PATH SUM 1

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

                3
            7       4
        2       4       6
    8       5       9       3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

TLDR.

NOTE: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge with a
triangle containing one-hundred rows; it cannot be solved by brute force,
and requires a clever method! ;o)
"""
import numpy as np

triangle_test = np.array([
[75, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
[95, 64, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
[17, 47, 82, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
[18, 35, 87, 10, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
[20, 4, 82, 47, 65, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
[19, 1, 23, 75, 3, 34, 00, 00, 00, 00, 00, 00, 00, 00, 00],
[88, 2, 77, 73, 7, 63, 67, 00, 00, 00, 00, 00, 00, 00, 00],
[99, 65, 4, 28, 6, 16, 70, 92, 00, 00, 00, 00, 00, 00, 00],
[41, 41, 26, 56, 83, 40, 80, 70, 33, 00, 00, 00, 00, 00, 00],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 00, 00, 00, 00, 00],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 00, 00, 00, 00],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 00, 00, 00],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 00, 00],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 00],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]])

# Now want to search down and through the array???????????????????
value_of_sum = 0 # Max value of traversed triangle

def max_path_sum(tri):
    for i in range(len(tri)-2, -1, -1): # Here we are moving up the triangle
        for j in range(i+1):
            # Max val is either above or above and across!
            tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])

    value_of_sum = tri[0][0]
    return value_of_sum

print(max_path_sum(triangle_test))





#end.
