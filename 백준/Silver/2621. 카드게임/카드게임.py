import sys
input = sys.stdin.readline

nums = [0] * 10
# red, blue, yellow, green
colors = [0] * 4
for _ in range(5):
    color, num = input().split()
    num = int(num)

    nums[num] += 1
    if color == 'R':
        colors[0] += 1
    elif color == 'B':
        colors[1] += 1
    elif color == 'Y':
        colors[2] += 1
    else:
        colors[3] += 1

score = 0
# 하이카드, 페어, 투페어, 트리플, 포카드
high = 0
dbh = 0
dbl = 0
tri = 0
four = 0
for i in range(9, 0, -1):
    if not high and nums[i]:
        high = i
    if nums[i] == 4:
        four = i
    elif nums[i] == 3:
        tri = i
    elif nums[i] == 2 and dbh == 0:
        dbh = i
    elif nums[i] == 2 and dbh:
        dbl = i

con_num = 0
cnt = 0

# 연속되는 수
for i in range(1, 10):
    if nums[i]:
        cnt += 1
        if cnt == 5:
            con_num = i
    elif not nums[i] and cnt:
        break

flush = 0
# 플러쉬
for c in colors:
    if c == 5:
        flush = 1
        break

# 스트레이트 플러쉬
if con_num and flush: 
    score = 900 + con_num
# 포카드
elif four:
    score = 800 + four
# 풀하우스
elif tri and dbh:
    score = 700 + 10 * tri + dbh
# 플러쉬
elif flush:
    score = 600 + high
# 스트레이트
elif con_num:
    score = 500 + con_num
# 트리플
elif tri:
    score = 400 + tri
# 투페어
elif dbh and dbl:
    score = 300 + 10 * dbh + dbl
# 페어
elif dbh:
    score = 200 + dbh
# 하이카드
else:
    score = 100 + high

print(score)
