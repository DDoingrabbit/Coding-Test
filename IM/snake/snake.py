n = int(input())
k = int(input())
apple = []
for _ in range(k):
    apple.append(list(map(int,input().split())))

l = int(input())
moves = []
for _ in range(l):
    x,c = input().split()
    moves.append([int(x),c])

board = [[0]*n for _ in range(n)]
for [i,j] in apple:
    board[i-1][j-1] = 1

snake = [[0,0]]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c):
    if c == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

count = 0
direction = 0
while True:
    if len(moves) !=0:
        if count == moves[0][0]:
            direction = turn(direction,moves[0][1])
            del moves[0]
    count +=1
    prev = snake[-1]
    head_x = prev[0]+dx[direction]
    head_y = prev[1]+dy[direction]
    if head_x<0 or head_y<0 or head_x>=len(board) or head_y >=len(board):
        print(count)
        break
    if [head_x,head_y] in snake:
        print(count)
        break
    if board[head_x][head_y] != 1:
        snake.append([head_x, head_y])
        del snake[0]
    else:
        snake.append([head_x, head_y])
        board[head_x][head_y] -=1