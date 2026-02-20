import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

answer = 4

for i in range(n):
    for j in range(m):
        # I
        if i + 3 < n:
            tmp = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 3][j]
            answer = max(answer,tmp)
        if j + 3 < m:
            tmp = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i][j + 3]
            answer = max(answer, tmp)
        # ㅁ
        if i + 1 < n and j + 1 < m:
            tmp = paper[i][j] + paper[i + 1][j] + paper[i][j + 1] + paper[i + 1][j + 1]
            answer = max(answer, tmp)
        # ㅗ
        if i - 1 >= 0 and j - 1 >= 0 and j + 1 < m:
            tmp = paper[i][j] + paper[i - 1][j - 1] + paper[i - 1][j] + paper[i - 1][j + 1]
            answer = max(answer, tmp)
        if i + 1 < n and j - 1 >= 0 and j + 1 < m:
            tmp = paper[i][j] + paper[i + 1][j - 1] + paper[i + 1][j] + paper[i + 1][j + 1]
            answer = max(answer, tmp)
        if j - 1 >= 0 and i - 1 >= 0 and i + 1 < n:
            tmp = paper[i][j] + paper[i - 1][j - 1] + paper[i][j - 1] + paper[i + 1][j - 1]
            answer = max(answer, tmp)
        if j + 1 < m and i - 1 >= 0 and i + 1 < n:
            tmp = paper[i][j] + paper[i - 1][j + 1] + paper[i][j + 1] + paper[i + 1][j + 1]
            answer = max(answer, tmp)
        # z
        if i + 2 < n and j + 1 < m:
            tmp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 2][j + 1]
            answer = max(answer, tmp)
        if i + 1 < n and j + 2 < m:
            tmp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j + 2]
            answer = max(answer, tmp)
        if i + 2 < n and j - 1 >= 0:
            tmp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j - 1] + paper[i + 2][j - 1]
            answer = max(answer, tmp)
        if i - 1 >= 0 and j + 2 < m:
            tmp = paper[i][j] + paper[i][j + 1] + paper[i - 1][j + 1] + paper[i - 1][j + 2]
            answer = max(answer, tmp)
        # L
        if i + 1 < n and j + 2 < m:
            tmp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2]
            answer = max(answer, tmp)
        if i + 1 < n and j - 2 >= 0:
            tmp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j - 1] + paper[i + 1][j - 2]
            answer = max(answer, tmp)
        if i - 1 > 0 and j + 2 < m:
            tmp = paper[i][j] + paper[i - 1][j] + paper[i - 1][j + 1] + paper[i - 1][j + 2]
            answer = max(answer, tmp)
        if i - 1 > 0 and j - 2 >= 0:
            tmp = paper[i][j] + paper[i - 1][j] + paper[i - 1][j - 1] + paper[i - 1][j - 2]
            answer = max(answer, tmp)
        if j + 1 < m and i + 2 < n:
            tmp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1]
            answer = max(answer, tmp)
        if j + 1 < m and i - 2 >= 0:
            tmp = paper[i][j] + paper[i][j + 1] + paper[i - 1][j + 1] + paper[i - 2][j + 1]
            answer = max(answer, tmp)
        if j - 1 >= 0 and i + 2 < n:
            tmp = paper[i][j] + paper[i][j - 1] + paper[i + 1][j - 1] + paper[i + 2][j - 1]
            answer = max(answer, tmp)
        if j - 1 >= 0 and i - 2 >= 0:
            tmp = paper[i][j] + paper[i][j - 1] + paper[i - 1][j - 1] + paper[i - 2][j - 1]
            answer = max(answer, tmp)
print(answer)
