import sys
input = sys.stdin.readline

n = int(input().strip())
building = list(map(int, input().split()))

def brute(idx):
    left = right = 0
    hl = hr = -float("inf")

    for i in range(idx - 1, -1, -1):
        tmp = (building[i] - building[idx]) / (idx - i)
        if hl >= tmp:
            continue
        left += 1
        hl = tmp
    
    for i in range(idx + 1, n):
        tmp = (building[idx] - building[i]) / (idx - i)
        if hr >= tmp:
            continue
        right += 1
        hr = tmp
    
    answer[idx] = left + right
    
answer = [0] * n

for i in range(n):
    brute(i)


print(max(answer))
