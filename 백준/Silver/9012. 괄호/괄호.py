T = int(input())

for t in range (T):
    ps = input()
    stack = []
    check = False

    for par in ps:
        if par == '(':
            stack.append(par)
        else:
            if stack:
                stack.pop()
                check = True
            else:
                check = False
                break
    
    if stack:
        check = False
    
    if check:
        print('YES')
    else:
        print('NO')