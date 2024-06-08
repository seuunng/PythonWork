import pandas as pd
import re, os

os.chdir(r'/Users/seunghee/PythonWork.py/CSVfile다루기')
df = pd.read_csv('apt2308.csv', encoding='cp949', thousands=',', on_bad_lines='skip')
# print(len(df))
# print(df.head()) # 처음 다섯개 행 출력
# print(df.tail()) # 마지막 다섯개 행 출력
# # 데이터프레임의 열 이름 출력
# print(df.columns)
# print(df['시군구'])
# # 조건별로 출력하기
# print(df['전용면적(㎡)']>80) # 면적이 80이 넘을땐 True, 아니라면 False
# # 0       False
# # 1       False
# # 2       False
# # 3        True
# print(df[df['전용면적(㎡)']>80]) 
# print(df['단지명'][df['전용면적(㎡)']>80]) 
# print(df['단지명'][(df['전용면적(㎡)']>80)&(df['거래금액(만원)']<30000)])
# 데이터 프레임에서 값을 선택할 때 조건을 더 정교하게 추가 하고 싶다면 loc를 사용
# print(df.loc[:10, ['단지명', '거래금액(만원)']]) #단지명과 거래금액만 10개 출력합니다.
# df['단가']=df['거래금액(만원)']/df['전용면적(㎡)']
# print(df.loc[:10, ('거래금액(만원)', '전용면적(㎡)','단가')])
# print(df.sort_values(by='거래금액(만원)').loc[:, ('거래금액(만원)', '시군구')])
# print(df.sort_values(by='거래금액(만원)', ascending=False).loc[:, ('거래금액(만원)', '시군구')])
# print(df[df['거래금액(만원)']>40000].sort_values(by='전용면적(㎡)').loc[:, ('거래금액(만원)', '전용면적(㎡)', '시군구')])
# 광진이 있으면 TRUE, 없으면 FALSE 
print(df['시군구'].str.contains('광진'))
#  광진이 있는 내역만 보여줌
print(df[df['시군구'].str.contains('광진')])
# 원하는 데이터만 들은 별도 객체에 저장
dfF=df[df['시군구'].str.contains('광진')]
print(dfF['거래금액(만원)'].mean())