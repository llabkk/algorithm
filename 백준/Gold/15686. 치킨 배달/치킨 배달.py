import sys
input = sys.stdin.readline

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def dfs(idx):
    global answer
    if len(survive) == M:
        dist = 0
        for r, c in house:
            tmp = INF
            for i, j in survive:
                tmp = min(tmp, abs(r - i) + abs(c - j))
            dist += tmp
        answer = min(answer, dist)
        return
    else:
        for i in range(idx + 1, cnt_chicken):
            survive.append(chicken[i])
            dfs(i)
            survive.pop()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
survive = []

for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            house.append((row, col))
        elif grid[row][col] == 2:
            chicken.append((row, col))

cnt_house = len(house)
cnt_chicken = len(chicken)

INF = float("inf")
answer = INF

dfs(-1)

print(answer)