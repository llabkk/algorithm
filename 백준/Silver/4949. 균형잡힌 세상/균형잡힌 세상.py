while True:
    sentence = input()
    if sentence == '.':
        break
    
    stack = []

    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
        elif s == '.':
            if stack:
                print('no')
                break
    else:
        print('yes')
