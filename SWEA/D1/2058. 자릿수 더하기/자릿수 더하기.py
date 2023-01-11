N = int(input())
sum = 0

while (N > 0):
    num = N % 10
    sum += num
    N //= 10

print(sum)