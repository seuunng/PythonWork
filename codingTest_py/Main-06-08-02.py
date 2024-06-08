import sys

# 제시될 수
N= int(sys.stdin.readline())
# N만큼 숫자 제공
arr=[]
for i in range(N):
    arr.append(int(sys.stdin.readline()))
# 배열 오름차순 정렬
arr2=sorted(arr)
# 배열 출력
for number in arr2:
    print(number)



