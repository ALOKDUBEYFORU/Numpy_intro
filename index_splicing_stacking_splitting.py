import numpy as np

array_1d = np.arange(10)
print('indexing of 1 d numpy array')
print(f'array_1d : {array_1d}')

print(f'0th element of array_1d[0] : {array_1d[0]}')
print(f'last element of array_1d[-1] : {array_1d[-1]}')

print('indexing of 2 d numpy array')
array_2d = np.arange(12).reshape(3,4)
print(f'printing array_2d : \n{array_2d}')
print(f'2nd column value in 1st row : {array_2d[1,2]}')
print(f'last column value in last row : {array_2d[-1,-1]}')

array_3d = np.arange(27).reshape(3,3,3)
print('indexing of 3 d numpy array')
print(f'array_3d : \n{array_3d}')
print(f'printing the value in the 1st row, 2nd column of 0th 2d matrix : {array_3d[0,1,2]}')
print(f'printing the value in the last row, last column of last 2d matrix : {array_3d[-1,-1,-1]}')

print('slicing of 1d numpy array')
print(f'array_1d : {array_1d}')

print(f'display the first three elements of array_1d[0:3] : {array_1d[0:3]}')
print(f'last two elements of array_1d[-1:-3:-1] : {array_1d[-1:-3:-1]}')
print(f'printing unordered elements like 2nd element, 4th element and last element : {array_1d[[1,3,-1]]}')

print('slicing of 2d numpy array')
print(f'printing array_2d : \n{array_2d}')

print(f'display of 1st row of array :{array_2d[0]}')
print(f'extracting 5,6,9,10 from array : \n{array_2d[1:,1:3]}')

print('slicing of 3d numpy array')
print(f'printing array_3d : \n{array_3d}')

print(f'extract 4,5,7,8 from 3d array : \n{array_3d[0,1:,1:]}')
print(f'extract 1st two element of first row in all the 2d matrices of 3d : \n{array_3d[:,0,0:2]}')

#array_vs1 contains the marks of three students in Maths, English and Social Science in an internal exam')
array_vs1 = np.array([[10,9,7],
                      [9,8,10],
                      [5,6,7]])

#array_vs2 contains the marks of another three students in Maths, English and social science.
array_vs2 = np.array([[2,5,10],
                      [9,8,9],
                      [7,7,7]])

print(f'Using Vstack method \n{array_vs1}  \n{array_vs2} \n{np.vstack((array_vs1,array_vs2))}')
print(f'Using hstack method to combine two numpy arrays horizontally. \n\n{array_vs1} \n\n{array_vs2} \n\n{np.hstack((array_vs1,array_vs2))}')

#Let us define  6*6 array and try to divide it into two arrrays using hsplit and vsplit.

array_cs = np.arange(36).reshape(6,6)
print(array_cs)

print(f'use hsplit to split array_cs into two parts :\n\n{np.hsplit(array_cs,2)}')

print(f'use vsplit to split array_cs into two parts :\n\n{np.vsplit(array_cs,2)}')