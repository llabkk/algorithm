T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    answer = 0
    speed = 0

    for _ in range(N):
        lst = list(map(int, input().split()))

        if lst[0] == 1:
            speed += lst[1]
        elif lst[0] == 2:
            speed -= lst[1]
            if speed < 0:
                speed = 0
        answer += speed
    print(f'#{test_case} {answer}')
