import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a = lst[0]
    b = lst[1]
    c = lst[2]
    if a == b == c and not a:
        break
    if a == b == c:
        print("Equilateral")
    elif c < b + a and a == b or b == c or c == a:
        print("Isosceles")
    elif c < b + a:
        print("Scalene")
    else:
        print("Invalid")
