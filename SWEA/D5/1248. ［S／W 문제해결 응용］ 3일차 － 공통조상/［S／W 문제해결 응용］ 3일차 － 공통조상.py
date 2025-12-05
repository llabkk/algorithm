def dfs(idx):
    global cnt
    cnt += 1

    for next_idx in child[idx]:
        dfs(next_idx)

    return

T = int(input())

for test_case in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())
    edges = list(map(int, input().split()))
    parents = [0] * (V + 1)
    child = [[] for _ in range(V + 1)]
    for i in range(E):
        parents[edges[2 * i + 1]] = edges[2 * i]
        child[edges[2 * i]].append(edges[2 * i + 1])
    a1 = []
    a2 = []
    goal = 0
    while goal != 1:
        a1.append(parents[n1])
        n1 = goal = parents[n1]

    goal = 0
    while goal != 1:
        a2.append(parents[n2])
        n2 = goal = parents[n2]

    answer1 = 0
    for i in a1:
        if answer1:
            break
        for j in a2:
            if i == j:
                answer1 = i
                break

    cnt = 0
    dfs(answer1)


    print(f'#{test_case} {answer1} {cnt}')