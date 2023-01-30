import sys
input = sys.stdin.readline

score = []
max_score = 0

for i in range (5):
    score.append(list(map(int, input().split())))
    sum_score = sum(score[i])

    if sum_score > max_score:
        max_score = sum_score
        winner = i+1

print(winner, max_score)