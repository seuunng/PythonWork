# 주어질 숫자의 개수
N= int(input())
# N개 숫자 배열에 입력하기
array=[]
for _ in range(N):
    element = int(input())
    array.append(element)
# 배열 순서 정렬해서 출력하기
array.sort()
for i in array:
    print(i)



    

