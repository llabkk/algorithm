import sys
input = sys.stdin.readline

def slide(idx, numbers):
    for i in range(N):
        if idx == 0:
            line = numbers[i]
            merge_line = merge(line)
            numbers[i] = merge_line
        elif idx == 1:
            line = [numbers[j][i] for j in range(N)]
            merge_line = merge(line)
            for j in range(N):
                numbers[j][i] = merge_line[j]
        elif idx == 2:
            line = numbers[i]
            merge_line = merge(line, True)
            numbers[i] = merge_line
        else:
            line = [numbers[j][i] for j in range(N)]
            merge_line = merge(line, True)
            for j in range(N):
                numbers[j][i] = merge_line[j]
    return numbers

def merge(line, reverse=False):
    original = []
    if reverse:
        line = line[::-1]

    for x in line:
        if x:
            original.append(x)

    merge_line = [0] * N
    idx = N - 1
    while original:
        num = original.pop()
        if merge_line[idx] == 0:
            merge_line[idx] = num
        elif merge_line[idx] == num:
            merge_line[idx] += num
            idx -= 1
        else:
            idx -= 1
            merge_line[idx] = num

    if reverse:
        merge_line = merge_line[::-1]
    return merge_line

def solve(cnt, numbers):
    global result
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                result = max(numbers[i][j], result)
        return
    for i in range(4):
        tmp = [numbers[x][:] for x in range(N)]
        tmp = slide(i, tmp)
        solve(cnt + 1, tmp)

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

start = ((0, 1), (0, 1), (N - 1, -1), (N - 1, -1))

result = 0

solve(0, grid)

print(result)
