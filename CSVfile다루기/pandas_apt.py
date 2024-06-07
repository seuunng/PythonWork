import pandas as pd
import re, os

os.chdir(r'/Users/seunghee/PythonWork.py/CSVfile다루기')
df = pd.read_csv('apt2308.csv', encoding='cp949', thousands=',', on_bad_lines='skip')
print(len(df))
print(df.head()) # 처음 다섯개 행 출력
print(df.tail()) # 마지막 다섯개 행 출력
# 데이터프레임의 열 이름 출력
print(df.columns)
print(df['시군구'])
# 조건별로 출력하기
print(df['전용면적(㎡)']>80) # 면적이 80이 넘을땐 True, 아니라면 False
# 0       False
# 1       False
# 2       False
# 3        True
print(df[df['전용면적(㎡)']>80]) 
print(df['단지명'][df['전용면적(㎡)']>80]) 
print(df['단지명'][(df['전용면적(㎡)']>80)&(df['거래금액(만원)']<30000)])