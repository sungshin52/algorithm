dice = list(map(int, input().split()))

if (dice[0] == dice[1] and dice[1] == dice[2]):
    prize = 10000 + dice[0] * 1000
    print(prize)

elif (dice[0] == dice[1] or dice[0] == dice[2]):
    prize = 1000 + dice[0] * 100
    print(prize)

elif (dice[1] == dice[2]):
    prize = 1000 + dice[1] * 100
    print(prize)

else:
    prize = max(dice) * 100
    print(prize)