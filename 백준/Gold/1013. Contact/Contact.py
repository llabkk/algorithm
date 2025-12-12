t = int(input())

for _ in range(t):
    ew = input()
    length = len(ew) - 1

    # 패턴이 유효한지 확인하는 변수
    answer = True

    # 0: 100+1+, 1:01, 3:None
    case = 3
    # 패턴에서 연속되는 0과 1의 개수
    one = 0
    zero = 0

    for i in range(length, -1, -1):
        if ew[i] == '1':
            # case == 0인 경우
            # case를 0으로 변환하는 기능은 else문에 있으므로 
            if zero > 1:
                case = 3
                zero = 0
                continue
            if one == 1 and zero == 1:
                one = 0
                zero = 0
            elif one > 1 and zero == 1:
                answer = False
                break
            one += 1
            if one == 1:
                case = 1
        else:
            if not case:
                pass
            elif not one:
                answer = False
                break
            zero += 1
            if zero > 1:
                case = 0
                one = 0
    if not(case == 3):
        if case == 1 and one == 1 and zero == 1:
            pass
        else:
            answer = False
    if answer:
        print('YES')
    else:
        print('NO')