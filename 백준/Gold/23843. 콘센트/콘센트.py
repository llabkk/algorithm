import sys
input = sys.stdin.readline

from collections import deque


n, m = map(int, input().split())
time = list(map(int, input().split()))
time.sort()

answer = 0
concent = deque([])

for i in range(n):
    power = time.pop()
    if len(concent) == m:
        base = concent.pop()
        for _ in range(m - 1):
            left = concent.popleft()
            left -= base
            if left > 0:
                concent.append(left)
        answer += base
    concent.append(power)

if concent:
    answer += concent[0]
print(answer)
