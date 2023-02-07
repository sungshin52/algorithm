import sys
input = sys.stdin.readline

n = int(input())
stick = []
cnt = 1

for _ in range (n):
    stick.append(int(input()))

max_stick = stick[-1]

for h in range (len(stick)-1, -1, -1):
    if stick[h] > max_stick:
        cnt += 1
        max_stick = stick[h]

print(cnt)