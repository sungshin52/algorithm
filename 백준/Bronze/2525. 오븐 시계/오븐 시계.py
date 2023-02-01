import sys
input = sys.stdin.readline

hour, min = map(int, input().split())
cook = int(input())

hour += cook // 60
min += cook % 60

if min >= 60:
    hour += min // 60
    min %= 60

if hour >= 24:
    hour %= 24

print(hour, min)