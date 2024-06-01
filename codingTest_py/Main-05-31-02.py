# 시리즈 넘버를 입력받음
N= int(input())

# '666'이 포함된 제목 중에서 N번째로 작은 수를 찾기
count=0
title=666
while True:
    if '666' in str(title):
        count += 1
        if N==count:
            break
    title+=1

print(title)


    

