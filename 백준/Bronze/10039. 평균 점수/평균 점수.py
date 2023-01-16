std = []

for i in range (5):
    score = int(input())
    
    if score < 40:
        std.append(40)
    else:
        std.append(score)

mean = int(sum(std) / len(std))
print(mean)