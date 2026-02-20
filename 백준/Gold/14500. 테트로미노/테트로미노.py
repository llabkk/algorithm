import sys
input = sys.stdin.readline

n, m = map(int, input().split())

paper = []
max_value = 0
for _ in range(n):
    row = list(map(int, input().split()))
    max_value = max(max_value, max(row))
    paper.append(row)

answer = 4

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

def dfs(block, ans, depth):
    global answer

    if answer >= ans + max_value * (4 - depth):
        return
    
    if depth == 4:
        answer = max(answer, ans)
        return
    for r, c in block:
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                dfs(block + [(nr, nc)], ans + paper[nr][nc], depth + 1)
                visited[nr][nc] = 0
    
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs([(i, j)], paper[i][j], 1)

print(answer)
