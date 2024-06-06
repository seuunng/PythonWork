import numpy as np

arr1 = np.array([[2,3,4],[6,7,8]])
arr2 = np.array([[10,10,10],[20,20,20]])

print(arr1+arr2)
# [[12 13 14]
#  [26 27 28]]
print(arr1*arr2)
# [[ 20  30  40]
#  [120 140 160]]
print(arr1/arr2)

arr3 = np.array([100, 200, 300])
print(arr1.shape) #(2, 3)
print(arr3.shape) #(3, )
print(arr1+arr3)
# [[102 203 304]
#  [106 207 308]]

arr4=np.arange(10)
print(arr4) # [0 1 2 3 4 5 6 7 8 9]
print(arr4[:5]) # [0 1 2 3 4]
print(arr4[-3:]) # [7 8 9]

