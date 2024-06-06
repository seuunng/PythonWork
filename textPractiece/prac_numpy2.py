import numpy as np
# numpy는 수치 계산을 위한 강력한 Python 라이브러리로, 
# 특히 다차원 배열 및 행렬 연산을 효율적으로 수행하는 데 사용됩니다. 
# 또한, 고성능의 수치 계산을 위한 다양한 수학 함수들을 제공합니다.

data = np.arange(1,5)
print(data.dtype)
print(data.astype('float64')) # 실수로 변경
print(data.astype('int32')) # 다시 정수로 변경

# 0으로 이뤄진 배열 만들기
print(np.zeros((2,10)))
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
print(np.ones((2,10)))
# [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
a=np.ones((2,3))
print(a)
# [[1. 1. 1.]
#  [1. 1. 1.]]
b=np.transpose(a)
print(b)
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]

