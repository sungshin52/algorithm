T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    max = nums[0]
    
    for i in range(1, len(nums)):
        if (nums[i] > max):
            max = nums[i]
    
    print(f'#{test_case} {max}')
