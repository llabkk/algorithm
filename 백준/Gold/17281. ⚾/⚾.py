import sys
input = sys.stdin.readline

from itertools import permutations


def baseball():
    b1 = b2 = b3 = 0
    score = num = out = 0
    for inning, mount in enumerate(player):
        if score + (N - inning) * 24 <= answer:
            break
        while inning < N:
            if mount[order[num]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif mount[order[num]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif mount[order[num]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif mount[order[num]] == 4:
                score += b1 + b2 + b3 + 1
                b1 = b2 = b3 = 0
            else:
                out += 1
                if out == 3:
                    out = 0
                    inning += 1
                    b1 = b2 = b3 = 0
                    num = (num + 1) % 9
                    break
            num = (num + 1) % 9
    return score

def solve():
    global N, player, order, answer
    N = int(input().strip())
    player = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for tmp in permutations(range(1, 9)):
        order = list(tmp)
        order = order[:3] + [0] + order[3:]
        current_score = baseball()
        answer = max(answer, current_score)
    print(answer)


solve()
