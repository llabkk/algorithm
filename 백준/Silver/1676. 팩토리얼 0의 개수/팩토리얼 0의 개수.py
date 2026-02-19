import sys
input = sys.stdin.readline

n = int(input().strip())

five = 0
for i in range(1, 1 + n):
    num = i
    while num != 0:
        if num % 5:
            break
        five += 1
        num //= 5
print(five)
