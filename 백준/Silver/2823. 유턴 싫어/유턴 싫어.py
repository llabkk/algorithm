import sys
input = sys.stdin.readline

from collections import deque

r, c = map(int, input().split())

grid = [input().strip() for _ in range(r)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

def bfs(row, col):
    que = deque([(row, col)])

    visited = [[0] * c for _ in range(r)]
    visited[row][col] = 1
    
    while que:
        y, x = que.popleft()

        path = 0
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < r and 0 <= nx < c and grid[ny][nx] == '.':
                path += 1
                if not visited[ny][nx]:
                    que.append((ny, nx))
                    visited[ny][nx] = 1
        else:
            if path <= 1:
                return 1
    return 0

answer = -1
for i in range(r):
    for j in range(c):
        if grid[i][j] == '.':
            answer = bfs(i, j)
            break
    if answer != -1:
        break

print(answer)