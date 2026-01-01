T = int(input())

for tc in range(1, 1 + T):
    stack = input()

    top = len(stack)
    cnt = 0
    while top:
        top -= 1
        temp = stack[top]

        if temp == ")":
            cnt += 1
        elif temp == "(":
            cnt -= 1

        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")