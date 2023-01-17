n = int(input())
num = n
count = 0

while True:
    sum = (num // 10) + (num % 10)
    new = ((num % 10) * 10) + (sum % 10)

    count += 1

    if new == n:
        break
    num = new

print(count)