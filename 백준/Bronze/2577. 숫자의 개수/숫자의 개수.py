A = int(input())
B = int(input())
C = int(input())

num_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
            '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

mul = str(A * B * C)

for i in mul:
    num_dict[i] += 1

for value in num_dict.values():
    print(value)