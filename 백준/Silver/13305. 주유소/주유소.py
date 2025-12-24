N = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = dists[0] * costs[0]
cost = costs[0]
dist = 0
for i in range(N - 1):
    if i > 0:
        dist += dists[i]
    if cost > costs[i + 1]:
        total += cost * dist
        cost = costs[i + 1]
        dist = 0
total += cost * dist
print(total)