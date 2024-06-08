# 응시한 학생 수와 수상 인원
N, k = map(int, input().split())
# 각 학생의 점수
arr = sorted(map(int, input().split()), reverse=True)
print(arr[k-1])



