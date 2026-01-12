import sys
input = sys.stdin.readline

from itertools import combinations

n = int(input().strip())

grid = [input().split() for _ in range(n)]

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

target = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'X':
            target.append((i, j))

answer = "NO"

def dfs():
    global answer
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'T':
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    while 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 'O':
                            break
                        if grid[ni][nj] == 'S':
                            return
                        ni += di
                        nj += dj
    answer = "YES"
    return

for a, b, c in combinations(target, 3):
    grid[a[0]][a[1]] = 'O'
    grid[b[0]][b[1]] = 'O'
    grid[c[0]][c[1]] = 'O'
    dfs()
    grid[a[0]][a[1]] = 'X'
    grid[b[0]][b[1]] = 'X'
    grid[c[0]][c[1]] = 'X'

print(answer)
