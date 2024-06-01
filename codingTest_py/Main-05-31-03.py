# 배달할 설탕의 양
N= int(input())

# 배달할 설탕봉지 계산하기
count=0
while N>=0:
    if N%5==0:
        count += N//5
        print(count)
        break
    N-=3
    count+=1
else : 
    if N < 0:    
        print(-1)



    

