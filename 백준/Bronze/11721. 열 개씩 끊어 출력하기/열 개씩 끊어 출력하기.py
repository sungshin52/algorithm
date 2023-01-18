string = input()

mul = len(string) // 10

for i in range (1, mul+1):
    print(string[(10 * (i - 1)) : (10 * i)])

print(string[(10 * mul) : ])