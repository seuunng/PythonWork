import sys

# N개 입력받기
N=int(sys.stdin.readline())
# N개만큼 좌표 입력받기
arr=[]
for i in range(N):
    a,b =map(int, sys.stdin.readline().strip().split())
    arr.append([a,b])
# 배열정렬
arr.sort(key=lambda x: (x[0], x[1]))
# 배열 출력
for coord in arr:
    print(*coord)