import sys

# 첫 번째 입력은 숫자의 개수 N
N= int(sys.stdin.readline())
# N만큼 숫자 제공
count = [0] * 10001 
for i in range(N):
    num=int(sys.stdin.readline())
    count[num] +=1
# 배열 오름차순 정렬
# arr.sort()
# 배열 출력
for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write(f"{i}\n")
