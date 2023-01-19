import sys

enter_leave = {}

n_record = int(sys.stdin.readline())

for _ in range (n_record):
    name, record = sys.stdin.readline().split()

    if record == 'enter':
        enter_leave[name] = record
    
    else:
        del enter_leave[name]

enter = sorted(enter_leave.keys(), reverse = True)

print(*enter, sep = '\n')