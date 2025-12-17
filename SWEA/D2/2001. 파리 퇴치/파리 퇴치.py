T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_death = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            death = 0
            for di in range(M):
                for dj in range(M):
                    ni = i + di
                    nj = j + dj
                    death += matrix[ni][nj]
            if max_death < death:
                max_death = death

    print(f"#{tc} {max_death}")
