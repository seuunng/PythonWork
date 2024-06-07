import numpy as np

discount = .05
cashflow = 100

# 자본의 현재가치를 구하는 공식을 함수로 만듭니단
def presentvalue(n):
    return (cashflow/((1+discount)**n))

print(presentvalue(1)) # 1년이 지났을 때 자본의 현재가치 입니다
print(presentvalue(2)) # 2년이 지났을 때 자본의 현재가치 입니다.

# 20년 동안 발생할 현재가치를 모두 한번에 구할 수도 있습니다.
for i in range(20):
    print(presentvalue(i))