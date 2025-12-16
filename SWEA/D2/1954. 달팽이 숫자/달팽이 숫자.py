T = int(input())

for tc in range(1, 1 + T):
    N = int(input())

    matrix = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    cnt = 0
    i = 0
    j = 0
    d = 0
    while cnt < N ** 2:
        cnt += 1
        matrix[i][j] = cnt

        ni = i + di[d]
        nj = j + dj[d]

        if not (0 <= ni < N and 0 <= nj < N) or matrix[ni][nj] != 0:
            d = (d + 1) % 4
            ni = i + di[d]
            nj = j + dj[d]
        i = ni
        j = nj

    print(f"#{tc}")
    for z in range(N):
        print(*matrix[z])
