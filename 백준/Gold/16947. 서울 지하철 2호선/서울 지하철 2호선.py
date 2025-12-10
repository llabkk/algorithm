import sys
input = sys.stdin.readline

# 최초 풀이
def check(start, prev):
    if len(edges[start]) == 1:
        return False

    for next_station in edges[start]:
        if next_station == prev:
            continue

        if cycle[next_station] == 1:
            continue

        if cycle[next_station] == -1:
            cycle[next_station] = 1
            cycle[start] = 1
            return True

        cycle[next_station] = -1

        if check(next_station, start):
            if cycle[start] == 1:
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

if len(cross):
    cycle[cross[0]] = -1
    check(cross[0], 0)

    for station in cross:
        if cycle[station] != 1:
            continue
        for next_station in edges[station]:
            if cycle[next_station] == 1:
                continue
            subway(next_station, station, 1)

print(*answer[1:])
