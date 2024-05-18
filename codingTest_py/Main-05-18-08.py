# O(g(n)) = {f(n) | 모든 n ≥ n에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n가 존재한다}
# f(n) = b * n + a, 양의 정수 c, n가 주어질 경우 O(n) 정의를 만족하는지 알아보자.
a, b = map(int, input().split())
c = int(input())
n = int(input())
if (a * n) + b <= c * n and a <= c:
    print(1)
else:
    print(0)

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if (a1 * n0) + a0 <= c * n0 and a1 <= c:
    print(1)
else:
    print(0)