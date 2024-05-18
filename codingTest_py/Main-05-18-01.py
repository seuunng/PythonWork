a, b, c = map(int, input().split())
longest = max(a, b, c)
if a+b>c and b+c>a and c+a>b :
    print(a+b+c)
else:
    if longest == a:
        a = b + c - 1
    elif longest == b:
        b = a + c - 1
    else:
        c = a + b - 1
    print(a + b + c)
