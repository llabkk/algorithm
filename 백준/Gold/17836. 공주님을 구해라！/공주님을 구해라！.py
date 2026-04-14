import sys
input = sys.stdin.readline

from collections import deque

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m, t = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    visited = [[0] * m for _ in range(n)]
    que = deque([(0, 0, 0, 0)])
    visited[0][0] = 1

    while que:
        r, c, time, sword = que.popleft()

        if time == t:
            return 0

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if nr == n - 1 and nc == m - 1:
                return time + 1
            if sword:
                if visited[nr][nc] == 2:
                    continue
                visited[nr][nc] = 2
                que.append((nr, nc, time + 1, 2))
            else:
                if visited[nr][nc]:
                    continue
                if grid[nr][nc] == 1:
                    continue
                elif grid[nr][nc] == 2:
                    visited[nr][nc] = 2
                    que.append((nr, nc, time + 1, 2))
                else:
                    visited[nr][nc] = 1
                    que.append((nr, nc, time + 1, 0))

answer = bfs()

if answer:
    print(answer)
else:
    print("Fail")
