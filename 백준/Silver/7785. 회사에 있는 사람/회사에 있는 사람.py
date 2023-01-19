enter_leave = {}

n_record = int(input())

for _ in range (n_record):
    name, record = input().split()

    if record == 'enter':
        enter_leave[name] = record
    
    else:
        del enter_leave[name]

enter = sorted(enter_leave.keys(), reverse = True)

print(*enter, sep = '\n')