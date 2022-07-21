# # 1712 손익분기점
#
# # 판매대수를 n이라고 설정
# # 손익분기점이 나지 않을 때는 -1 출력해야 한다.
# # A / (C - B)가 음수이면, 결코 손익분기점에 도달할 수 없다.
# # 예: A=3, B=2, C=1 일 때 n > 2n + 3을 따져보면 n < -3으로 음수이다.
# # 즉 A / (C - B)일 경우, 물건을 생산하면 오히려 손해가 된다.
#
# # A, B, C = map(int, input().split())
# #
# # n = 1
# # profit = n * C
# # loss = n * B + A
# #
# # if (A / (C - B) < 0) :
# #     print(-1)
# # else:
# #     while True:
# #         profit = n * C
# #         loss = n * B + A
# #         if profit > loss:
# #             print(n)
# #             break
# #         else:
# #             n += 1
#
# # 위에처럼 짰더니 코드는 정상작동하는데, 예제 3번의 A:2100000000 이게 값이 너무 커서
# # 시스템이 멈춰버렸다. 그래서 다르게 접근할 필요를 느낌
# # 아까 앞에서 A / (C - B) 이 값이 0보다 작으면 손익분기점 결코 넘을 수 없다고 했다.
# # 그럼 손익분기점을 넘는 수는, 저 수에 +1을 하면 되지 않을까? 하고 다시 코드를 짰다.
# # 만약 A / (C-B)가 float형으로 소수점이 붙어있을 경우에는, +1을 한 값에 소수점을 floor로 버린다.
# # 가령 4.5 < n일 경우 n이 4.5+1 = 5.5인 상태에서 0.5를 버림한다.
# # 5개부터 손익분기점을 넘길 수 있다는 것이므로.
#
# # import math
# #
# # A, B, C = map(int, input().split())
# #
# # n = 1
# # profit = n * C
# # loss = n * B + A
# #
# # if (A // (C - B) < 0) :
# #     print(-1)
# # else:
# #     n = (A // (C - B)) + 1
# #     print(math.floor(n))
#
# # 그랬더니 ZeroDivisionError가 떠버렸다.
# # -1이 결과값이 되는 상황 중 3+n < n인 상황도 있을거다.
# # 그래서 그런 케이스를 하나 더 조건에 추가해줬다.
#
# import math
#
# A, B, C = map(int, input().split())
#
# n = 1
# profit = n * C
# loss = n * B + A
#
# if (C - B) == 0:
#     print(-1)
# elif (A // (C - B) < 0) :
#     print(-1)
# else:
#     n = (A // (C - B)) + 1
#     print(math.floor(n))


# 2292 벌집
# 이건 규칙성을 따져보면 쉽게 풀 수 있는데, 벌집의 숫자는 6의 배수로 늘어난다.
# 가령 1은 6의 0제곱, 1을 둘러싼 원은 2-7(6개), 그 다음 원은 8-19(12개), 다음 원은 20-37(18개)...
# 이걸 레벨별로 정리하면, level 1은 6의 0제곱, 2레벨은 1레벨 + 6의 1제곱 범위 내, 3레벨은 2레벨 6의 2제곱 범위 내
# 재귀 함수로 만들어놓고 나중에 return 값으로 cnt를 받으니까 None이 떠서 왜이러지 한참 고민했다
# 1레벨로 다시 돌아왔을 때 return 값이 없으니까!!

def find_loc(start, cnt):
    global ret_cnt
    for i in range(1, 6 * cnt + 1):
        if start + i == N:
            ret_cnt = cnt
            return
        if i == 6 * cnt:
            start += i

    find_loc(start, cnt + 1)
    return


N = int(input())
ret_cnt = 0
if N == 1:
    print(1)
else:
    find_loc(1, 1)
    print(ret_cnt+1)


# 근데 이렇게 풀었더니 RecursionError가 나옴
# RecursionError는 최대 재귀 깊이를 넘었을 때 발생하는 현상이다.