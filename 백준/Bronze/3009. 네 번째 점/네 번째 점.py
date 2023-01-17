x_sqr = []
y_sqr = []

for i in range (3):
    x, y = list(map(int, input().split()))
    x_sqr.append(x)
    y_sqr.append(y)

for i in range (3):
    if x_sqr.count(x_sqr[i]) == 1:
        x = x_sqr[i]

    if y_sqr.count(y_sqr[i]) == 1:
        y = y_sqr[i]

print(x, y)