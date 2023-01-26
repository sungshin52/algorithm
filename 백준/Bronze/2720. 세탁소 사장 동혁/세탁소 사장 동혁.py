import sys

T = int(sys.stdin.readline())

for t in range (T):
    money = int(sys.stdin.readline())

    quarter = money // 25
    dime = (money % 25) // 10
    nickel = ((money % 25) % 10) // 5
    penny = ((money % 25) % 10) % 5

    print(f'{quarter} {dime} {nickel} {penny}')