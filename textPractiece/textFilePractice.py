import re
word=['apple', 'cat', 'brave', 'drama', 'arise', 'blow', 'coat', 'above']
for i in word:
    m = re.match(r'a\D+',i)
    if m: print(m.group())

a="제 이메일 주소는 greatking@naver.com압나다. 오늘 저는 travel@daum.net라는 주소로 메일을 보내려고 합니다. 저는 apple@gamil.com, life@abc.co.kr라는 메일도 사용하고 있습니다."
b=re.findall(r'[a-z]+@[a-z]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?',a)
#(?: ... )? 있으면 출력 없으면 말고
print(b)

exam='저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2020년 입니다.'
answer=re.findall(r'[0-9]{2,4}년', exam)
print(answer)

d='I have a dog. I am not a girl. You are not alone. I am happy.'
e=re.findall(r'[^.]+\.', d)a
print(e)

f='Chandler: Allright Joey, be nice. So does he have a hump? A hump and a hairpiece? Phebe: Wait, does he eat chalk? Phebe: Just, because, I dont want her to go through what I went through with Carl- oh!'
g=re.findall(r'[A-Za-z]+\:', f)
print(g)
G=list(set(g))
print(G)

import usecsv

