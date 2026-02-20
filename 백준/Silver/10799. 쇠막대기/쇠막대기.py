import sys
input = sys.stdin.readline

ironbar = input().strip()

answer = bar = 0
prev = None

for iron in ironbar:
    if iron == '(':
        bar += 1
    elif iron == ')':
        bar -= 1
        if prev == '(':
            answer += bar
        else:
            answer += 1
    prev = iron

print(answer)
