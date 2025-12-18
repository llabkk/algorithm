import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def dijkstra():
    start = [(0, 1)]
    while start:
        dist, prev = heappop(start)

        for nxt, nxt_dist in edges[prev]:
            new_dist = dist + nxt_dist

            if len(answer[nxt]) == K:
                origin = -heappop(answer[nxt])
                if origin > new_dist:
                    heappush(answer[nxt], -new_dist)
                    heappush(start, (new_dist, nxt))
                else:
                    heappush(answer[nxt], -origin)
            else:
                heappush(answer[nxt], -new_dist)
                heappush(start, (new_dist, nxt))

N, M, K = map(int, input().split())

edges = [[] for _ in range(N + 1)]
answer = [[] for _ in range(N + 1)]
heappush(answer[1], 0)

check = set()

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

dijkstra()

for i in range(1, 1 + N):
    if len(answer[i]) < K:
        print(-1)
    else:
        print(-heappop(answer[i]))
