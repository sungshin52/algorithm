N = int(input())
customer = list(map(int, input().split()))

cnt = 0

for cus in range (min(customer), max(customer) + 1):
    if customer.count(cus) > 1:
        cnt += customer.count(cus) - 1

print(cnt)