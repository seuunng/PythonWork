# 5개 숫자 배열에 입력하기
array=[]
for _ in range(5):
    element = int(input())
    array.append(element)
# 평균과 중앙값 구하기
array.sort()
sum=0
for i in array:
    sum += i
avg=sum//5
mid=array[2]

print(avg)
print(mid)


    

