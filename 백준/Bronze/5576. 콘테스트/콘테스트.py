import sys
input = sys.stdin.readline

scores_W = []
scores_K = []

for _ in range (10):
    scores_W.append(int(input()))

for _ in range (10):
    scores_K.append(int(input()))

scores_W.sort(reverse = True)
scores_K.sort(reverse = True)

print(sum(scores_W[:3]), sum(scores_K[:3]))