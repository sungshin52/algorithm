T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    sum = 0
    
    for num in nums:
        sum += num
        
    average = round(sum / 10)
    print(f'#{test_case} {average}')
