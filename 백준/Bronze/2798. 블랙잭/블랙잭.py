import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0

for i in range (N-2):
    for j in range (i+1, N-1):
        for k in range (j+1, N):
            sum = cards[i] + cards[j] + cards[k]

            if max_sum < sum <= M:
                max_sum = sum
            
            if sum == M:
                max_sum = sum
                break

print(max_sum)