M = int(input())
Narr =[]

# 숫자를 문자열로 변환한 후 한 자리씩 자르기
for number in range(1, M + 1):
    digits = [int(digit) for digit in str(number)]
    D=sum(digits)
    if M == number + D:
        Narr.append(number)

if Narr:
    N = min(Narr)
    print(N)
else:
    print(0)
        

