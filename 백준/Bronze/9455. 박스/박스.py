import sys
input = sys.stdin.readline

T = int(input())

for _ in range (T):
    m, n = map(int, input().split())
    box = []
    cnt = 0
    for _ in range (m):
        box.append(list(map(int, input().split())))
    
    for col in range (n):
        cnt_temp = 0

        for row in range (m-1, -1, -1):
            if (box[row][col] == 1):
                cnt += cnt_temp
            
            else:
                cnt_temp += 1
    
    print(cnt)