while(True):
    string = input()

    if string == '.':
        break

    stack = []
    result = True

    for elem in string:
        if elem == '(' or elem =='[':
            stack.append(elem)
        
        elif elem == ')':
            if len(stack) == 0 or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
        
        elif elem == ']':
            if len(stack) == 0 or stack[-1] == '(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
    
    if len(stack) == 0 and result == True:
        print('yes')
    else:
        print('no')
