import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())

arr = [0] * 2 * n
visited = [0] * (n + 1)

tmp = y - x - 1

arr[x - 1] = tmp
arr[y - 1] = tmp
visited[tmp] = 1

def lang(idx):
    global answer

    if idx == 2 * n:
        for num in arr:
            if not num:
                return
        answer += 1
        return

    if arr[idx]:
        lang(idx + 1)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        if idx + i + 1 < 2 * n and not arr[idx + i + 1]:
                arr[idx] = i
                arr[idx + i + 1] = i
                visited[i] = 1
                lang(idx + 1)
                arr[idx] = 0
                arr[idx + i + 1] = 0
                visited[i] = 0


answer = 0

lang(0)

print(answer)
