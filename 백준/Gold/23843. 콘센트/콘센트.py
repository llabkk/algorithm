import sys
input = sys.stdin.readline

from heapq import heappop, heappush

n, m = map(int, input().split())
time = list(map(int, input().split()))

time.sort(reverse=True)

heap = [0] * m

for i in range(n):
    base = heappop(heap)
    heappush(heap, base + time[i])

print(max(heap))
