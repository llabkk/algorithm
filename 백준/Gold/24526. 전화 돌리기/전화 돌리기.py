import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)

# 0 = 미방문
# 1 = 탐색 중 (스택)
# 2 = 처리 완료
state = [0] * (n + 1)

# 1 = 제거 대상 (사이클 또는 도달)
bad = [0] * (n + 1)


for start in range(1, n + 1):
    if state[start]:
        continue

    stack = [(start, 0)]
    state[start] = 1

    while stack:
        u, idx = stack[-1]

        if idx < len(edges[u]):
            v = edges[u][idx]
            stack[-1] = (u, idx + 1)

            if state[v] == 0:
                state[v] = 1
                stack.append((v, 0))

            elif state[v] == 1:
                bad[u] = 1    # 사이클 발견

            else:  # state[v] == 2
                if bad[v]:
                    bad[u] = 1

        else:
            stack.pop()
            state[u] = 2
            if stack and bad[u]:
                parent, _ = stack[-1]
                bad[parent] = 1


answer = -1
for num in bad:
    if not num:
        answer += 1
print(answer)
