import sys
input = sys.stdin.readline

from collections import deque

n = int(input().strip())

balloon = deque(map(int, input().split()))
idx = deque(range(n))

answer = []

while True:
    cnt = balloon.popleft()
    answer.append(idx.popleft() + 1)

    if not balloon:
        break

    if cnt > 0:
        for i in range(cnt - 1):
            tmp = balloon.popleft()
            balloon.append(tmp)

            tmp2 = idx.popleft()
            idx.append(tmp2)

    else:
        for i in range(-cnt):
            tmp = balloon.pop()
            balloon.appendleft(tmp)

            tmp2 = idx.pop()
            idx.appendleft(tmp2)

print(*answer)
