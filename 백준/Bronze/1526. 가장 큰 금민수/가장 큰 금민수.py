import sys
input = sys.stdin.readline

nums = int(input())

while 1:
    check = True

    for num in str(nums):
        if (num != '4') and (num != '7'):
            check = False
            nums -= 1
    
    if check:
        print(nums)
        break