for _ in range(10):
    test_case = int(input())
    N, M = map(int, input().split())
    answer = N ** M
    print(f'#{test_case} {answer}')