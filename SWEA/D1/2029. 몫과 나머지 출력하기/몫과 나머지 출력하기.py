T = int(input())

for test_case in range(1, T + 1):
    a, b = list(map(int, input().split()))
    share = a // b
    left = a % b
    print(f'#{test_case} {share} {left}')