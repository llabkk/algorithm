T = int(input())

for _ in range(T):
    N = int(input())

    dp = [0] * (N + 1)
    dp[0] = (1, 0)

    if N > 0:
        dp[1] = (0, 1)

    if N > 1:
        for i in range(2, N + 1):
            l0, l1 = dp[i - 2]
            r0, r1 = dp[i - 1]
            dp[i] = (l0 + r0, l1 + r1)

    print(*dp[N])