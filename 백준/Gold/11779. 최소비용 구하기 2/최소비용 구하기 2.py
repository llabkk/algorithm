import sys
input = sys.stdin.readline

from heapq import heappop, heappush

from copy import deepcopy

INF = float("inf")

def dijkstra(start):
    dists = [(INF, 0)] * (n + 1)
    dists[start] = (0, [start])
    pq = [(0, start)]

    while pq:
        dist, node = heappop(pq)

        if dists[node][0] < dist:
            continue

        for nxt, ndist in edges[node]:
            pdist = dist + ndist
            if dists[nxt][0] <= pdist:
                continue
            heappush(pq, (pdist, nxt))
            tmp = deepcopy(dists[node][1])
            tmp.append(nxt)
            dists[nxt] = (pdist, tmp)
    return dists

n = int(input().strip())
m = int(input().strip())

edges = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    edges[s].append((e, d))

enter, goal = map(int, input().split())

answer = dijkstra(enter)

print(answer[goal][0])
print(len(answer[goal][1]))
print(*answer[goal][1])
