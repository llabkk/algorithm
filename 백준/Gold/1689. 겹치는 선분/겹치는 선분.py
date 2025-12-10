import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input().strip())

# N이 1이면 선분 하나 읽고 바로 1 출력
if N == 1:
    s, e = map(int, input().split())
    print(1)
    sys.exit(0)

start = []
end = []
for _ in range(N):
    s, e = map(int, input().split())
    heappush(start, s)
    heappush(end, e)

point = front = heappop(start)
rear = heappop(end)
answer = tmp = 0

while start or end:
    while start and point == front:
        tmp += 1
        front = heappop(start)

    if not start and point == front:
        tmp += 1
        front = 1000000001

    while end and point == rear:
        tmp -= 1
        rear = heappop(end)

    if not end and point == rear:
        tmp -= 1
        rear = 1000000001

    point = min(front, rear)
    answer = max(answer, tmp)

print(answer)
