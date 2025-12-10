import sys
input = sys.stdin.readline

N = int(input())
points = []

for _ in range(N):
    s, e = map(int, input().split())
    points.append((s, 1))   # 시작점: +1
    points.append((e, -1))  # 끝점: -1

points.sort()  # 좌표 기준, 같은 좌표면 -1이 1보다 먼저 옴

cnt = 0
answer = 0
for x, v in points:
    cnt += v          # 현재 위치에서 겹치는 선분 개수
    if cnt > answer:
        answer = cnt  # 최대값 갱신

print(answer)
