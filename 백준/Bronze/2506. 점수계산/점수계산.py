N = int(input())
result = list(map(int, input().split()))
sum = 0
score = 0

for i in range (N):
    if (result[i] == 1):
        sum += 1
        score += sum
    
    else:
        sum = 0

print(score)