import sys
input = sys.stdin.readline

def check(start, prev):
    if len(edges[start]) == 1:
        return False

    for next_station in edges[start]:
        if next_station == prev:
            continue

        if cycle[next_station]:
            continue

        if visited[next_station]:
            cycle[next_station] = 1
            cycle[start] = 1
            return True

        visited[next_station] = 1

        if check(next_station, start):
            if cycle[start]:
                return False
            cycle[start] = 1
            return True
    return False

def subway(start, prev, dist):
    answer[start] = dist
    if len(edges[start]) == 1:
        return

    for next_station in edges[start]:
        if next_station == prev:
            continue
        subway(next_station, start, dist + 1)
    return

N = int(input().strip())

edges = [[] for _ in range(N + 1)]
for i in range(N):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

cross = []
answer = [0] * (N + 1)
cycle = [0] * (N + 1)

for i in range(1, N + 1):
    if len(edges[i]) > 2:
        cross.append(i)

for station in cross:
    if cycle[station]:
        continue
    visited = [0] * (N + 1)
    visited[station] = 1
    check(station, 0)

for station in cross:
    if not cycle[station]:
        continue
    for next_station in edges[station]:
        if cycle[next_station]:
            continue
        subway(next_station, station, 1)

print(*answer[1:])
