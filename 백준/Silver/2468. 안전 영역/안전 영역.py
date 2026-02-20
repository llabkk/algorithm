import sys
input = sys.stdin.readline

from collections import deque

n = int(input().strip())
city = [list(map(int, input().split())) for _ in range(n)]

minh = 100
maxh = 1
for high in city:
    minh = min(minh, min(high))
    maxh = max(maxh, max(high))

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def check(row, col):
    return 0 <= row < n and 0 <= col < n

def bfs(row, col, limit):
    visited[row][col] = 1
    que = deque([(row, col)])

    while que:
        r, c = que.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if not check(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if city[nr][nc] < limit:
                continue
            visited[nr][nc] = 1
            que.append((nr, nc))
    
            

answer = 1

for k in range(minh, maxh + 1):
    visited = [[0] * n for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if city[i][j] >= k:
                tmp += 1
                bfs(i, j, k)
            else:
                visited[i][j] = 1
    answer = max(answer, tmp)

print(answer)
