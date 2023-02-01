import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
series = 666

while 1:
    if '666' in str(series):
        cnt += 1
    
    if cnt == N:
        print(series)
        break
    
    series += 1