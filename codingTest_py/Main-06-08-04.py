import sys
# 숫자 입력 받기
# input = sys.stdin.read
# 전체 입력
n=sys.stdin.readline().rstrip()
# 입력된 숫자 잘라서 배열어 넣기
arr = list(n)
# 배열정렬
arr.sort(reverse=True)
# 배열 출력
print(''.join(arr))