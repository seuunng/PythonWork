import numpy as np

a = np.array([[2, 3], [5, 2]])
print(a)

b = np.array([[1,2,3,4,5],[2,4,6,8,10],[5,6,7,8,9]])
print(b[0][2])
print(b[0,2])
print(b[2:,2:]) # 7 8 9

c = np.array([2,3,4,5,6,7])
print(c) #2 3 4 5 6
print(c.shape) # (6,)

d = np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(d.shape) # (2, 5)

print(c.dtype) #int64 : 정수로 이뤄졌다는 의미
print(d.dtype) #int64 : 정수로 이뤄졌다는 의미

