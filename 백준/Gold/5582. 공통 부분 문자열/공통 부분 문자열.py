import sys

input = sys.stdin.readline


first = input().strip()
second = input().strip()

f_len = len(first)
s_len = len(second)

curr = [0] * (s_len + 1)
prev = [0] * (s_len + 1)


answer = 0

for i in range(1, f_len + 1):
    for j in range(1, s_len + 1):
        if first[i - 1] == second[j - 1]:
            curr[j] = prev[j - 1] + 1
            answer = max(answer, curr[j])
    prev = curr
    curr = [0] * (s_len + 1)

print(answer)
