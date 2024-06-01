
def count_false(board, x, y, start_char):
    count=0
    for i in range(8):
        for j in range(8):
            if(i+j)%2==0:
                expected_char = start_char
            else:
                if start_char == 'W':
                    expected_char = 'B'
                else:
                    expected_char = 'W'
            if board[i+x][j+y] != expected_char:
                count+=1
    return count

def min_repaints(board, n,m):
    count_min = float('inf') #파이썬에서 무한대를 나타내는 방법
    for i in range(n-7):
        for j in range(m-7):
            startting_W=count_false(board, i, j,'W')
            startting_B=count_false(board, i, j,'B')
            count_min=min(count_min, startting_W, startting_B)
    return count_min
    
# 체스판의 규격을 입력받음
a, b = map(int, input().split())

# a*b 2차 배열
board=[]
for i in range(a):
    board.append(input().strip())

print(min_repaints(board,a,b))


    

