import sys
input = sys.stdin.readline

from collections import deque

t = int(input().strip())

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(row, col):
    answer = 1
    que = deque([(row, col)])
    visited[row][col] = 1
    
    while que:
        r, c = que.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if nr > 2 or nr < 0 or nc > 2 or nc < 0:
                continue
            if visited[nr][nc]:
                continue
            if choco[nr][nc] == 'O':
                visited[nr][nc] = 1
                que.append((nr, nc))
                answer += 1
    return answer
    
for tc in range(t):
    choco = []
    for _ in range(3):
        tmp = input().strip()
        choco.append(tmp)
    cnt = list(map(int, input().split()))

    visited = [[0]*3 for _ in range(3)]
    visited[1][1] = 1

    score = []
    for i in range(3):
        for j in range(3):
            if visited[i][j]:
                continue
            if choco[i][j] != 'O':
                visited[i][j] = 1
                continue
            score.append(bfs(i, j))
    score.sort()
    
    if cnt[0] != len(score):
        print(0)
        continue

    for i in range(cnt[0]):
        if cnt[i + 1] != score[i]:
            print(0)
            break
    else:
        print(1)
