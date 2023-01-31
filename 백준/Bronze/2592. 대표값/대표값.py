import sys
input = sys.stdin.readline

nums = []
freq = 0

for _ in range (10):
    num = int(input())
    nums.append(num)

    if nums.count(num) > freq:
        freq = nums.count(num)
        freq_num = num

print(sum(nums) // len(nums))
print(freq_num)