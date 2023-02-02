import sys
input = sys.stdin.readline

ball = 1

for _ in range (int(input())):
    x, y = map(int, input().split())

    if (x == ball) or (x == y == ball):
        ball = y
    
    elif (y == ball):
        ball = x

print(ball)