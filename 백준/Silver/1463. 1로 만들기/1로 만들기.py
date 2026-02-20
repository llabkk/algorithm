import sys
input = sys.stdin.readline

from collections import deque

n = int(input().strip())

visited = [0] * (n + 1)

que = deque([(n, 0)])

while que:
    num, answer = que.popleft()

    if num == 1:
        print(answer)
        break

    if num % 3 == 0 and not visited[num // 3]:
        visited[num // 3] = 1
        que.append((num // 3, answer + 1))
    
    if num % 2 == 0 and not visited[num // 2]:
        visited[num // 2] = 1
        que.append((num // 2, answer + 1))
    if not visited[num - 1]:
        visited[num - 1] = 1
        que.append((num - 1, answer + 1))