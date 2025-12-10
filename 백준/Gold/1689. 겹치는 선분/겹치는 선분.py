import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input().strip())
lines = []
for _ in range(N):
    s, e = map(int, input().split())
    heappush(lines, (s, 1))
    heappush(lines, (e, -1))

answer = tmp = 0


while lines:
    _, score = heappop(lines)

    tmp += score

    answer = max(answer, tmp)

print(answer)
