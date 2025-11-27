import sys

input = sys.stdin.readline

H, W, N, M = map(int, input().split())

r = c = 1
r += (H - 1) // (N + 1)
c += (W - 1) // (M + 1)

print(r * c)