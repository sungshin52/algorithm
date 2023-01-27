left_list = []

for _ in range (10):
    num = int(input())
    left = num % 42

    if left not in left_list:
        left_list.append(left)

print(len(left_list))