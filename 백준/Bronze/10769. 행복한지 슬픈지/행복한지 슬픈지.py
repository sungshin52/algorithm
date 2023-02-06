import sys
input = sys.stdin.readline

emoji = input()

happy = emoji.count(':-)')
sad = emoji.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy < sad:
    print('sad')
elif happy > sad:
    print('happy')
elif happy == sad:
    print('unsure')
