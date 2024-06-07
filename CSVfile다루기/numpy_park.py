import numpy as np
import numpy_financial as npf
# 금융관련 함수만 별도의 패키지로 분리
# 순현재가치
# npf.npv(할인율, 현금 흐름)
# 내부수익률
# npf.irr(현금흐름)

loss = [-750]
profit = [100]*10
cf = loss+profit
print(len(cf)) #cf에 몇개의 정보가 있는지 확인
cashflow = np.array(cf)

# 순현재가치
npv = npf.npv(0.045, cashflow)
print(npv) 
# 내부수익률
irr = npf.irr(cashflow)
print(irr)