# # 1712 손익분기점
#
# # 판매대수를 n이라고 설정
# # 손익분기점이 나지 않을 때는 -1 출력해야 한다.
# # A / (C - B)가 음수이면, 결코 손익분기점에 도달할 수 없다.
# # 예: A=3, B=2, C=1 일 때 n > 2n + 3을 따져보면 n < -3으로 음수이다.
# # 즉 A / (C - B)일 경우, 물건을 생산하면 오히려 손해가 된다.
#
# A, B, C = map(int, input().split())
#
# n = 1
# profit = n * C
# loss = n * B + A
#
# if (A / (C - B) < 0) :
#     print(-1)
# else:
#     while True:
#         profit = n * C
#         loss = n * B + A
#         if profit > loss:
#             print(n)
#             break
#         else:
#             n += 1
#
# # 위에처럼 짰더니 코드는 정상작동하는데, 예제 3번의 A:2100000000 이게 값이 너무 커서
# # 시스템이 멈춰버렸다. 그래서 다르게 접근할 필요를 느낌
# # 아까 앞에서 A / (C - B) 이 값이 0보다 작으면 손익분기점 결코 넘을 수 없다고 했다.
# # 그럼 손익분기점을 넘는 수는, 저 수에 +1을 하면 되지 않을까? 하고 다시 코드를 짰다.
# # 만약 A / (C-B)가 float형으로 소수점이 붙어있을 경우에는, +1을 한 값에 소수점을 floor로 버린다.
# # 가령 4.5 < n일 경우 n이 4.5+1 = 5.5인 상태에서 0.5를 버림한다.
# # 5개부터 손익분기점을 넘길 수 있다는 것이므로.
#
# import math
#
# A, B, C = map(int, input().split())
#
# n = 1
# profit = n * C
# loss = n * B + A
#
# if (A // (C - B) < 0) :
#     print(-1)
# else:
#     n = (A // (C - B)) + 1
#     print(math.floor(n))
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


# # 2292 벌집
# # 이건 규칙성을 따져보면 쉽게 풀 수 있는데, 벌집의 숫자는 6의 배수로 늘어난다.
# # 가령 1은 6의 0제곱, 1을 둘러싼 원은 2-7(6개), 그 다음 원은 8-19(12개), 다음 원은 20-37(18개)...
# # 이걸 레벨별로 정리하면, level 1은 6의 0제곱, 2레벨은 1레벨 + 6 * 1 범위 내, 3레벨은 2레벨 + 6* 2의 범위 내
# # 재귀 함수로 만들어놓고 나중에 return 값으로 cnt를 받으니까 None이 떠서 왜이러지 한참 고민했다
# # 1레벨로 다시 돌아왔을 때 return 값이 없으니까!!
#
# def find_loc(start, cnt):
#     global ret_cnt
#     for i in range(1, 6 * cnt + 1):
#         if start + i == N:
#             ret_cnt = cnt
#             return
#         if i == 6 * cnt:
#             start += i
#
#     find_loc(start, cnt + 1)
#     return
#
#
# N = int(input())
# ret_cnt = 0
# if N == 1:
#     print(1)
# else:
#     find_loc(1, 1)
#     print(ret_cnt+1)
#
#
# # 근데 이렇게 풀었더니 RecursionError가 나왔다.
# # RecursionError는 최대 재귀 깊이를 넘었을 때 발생하는 현상이다.
# # 레벨의 마지막 값들이 1, 7, 19, 37...인데 이 수들은 전부 -1 하면 6*0, 6*1, 6*2...이다.
# # 즉 들어온 수 n이 6 * ? -1 이하일 때 이 ?가 뭔지만 확인하면 된다.
#
# n = int(input())
# i = 0
# while (6 * i) + 1 <= n:
#     i += 1
#
# print(i)
#
# # 근데 저 위에것도 시간초과가 나왔다.
# # 그래서 아래처럼 바꿨더니 드디어 통과
# # 생각해보니 위에거는 아예 식을 잘못 짰다. (6 * i) + 1이 각 층의 마지막 수가 아니라
# # 마지막 수에 계속 더해지는 식으로 짰어야 했는데.
#
# n = int(input())
# cnt = 0
# final_room_num = 1
# while n > final_room_num:
#     cnt += 1
#     final_room_num += 6 * cnt
#
# print(cnt + 1)

# # 1193 분수 찾기
# def find_num(y, x, cnt, str):
#     dy = [1, -1]
#     dx = [-1, 1]
#
#     if cnt == N:
#         print(arr[y][x], end='')
#         return
#
#
#     # case [0] 좌하향
#     # case [1] 우상향
#
#     for i in range(2):
#         if (y + dy[i]) + (x + dx[i]) == y + x:
#             if y + dy[i] < 0 or x + dx[i] < 0 :continue
#             if y + dy[i] >= 10000 or x + dx[i] >= 10000 :continue
#             if MAP[y + dy[i]][x + dx[i]] == -1: continue
#             MAP[y + dy[i]][x + dx[i]] = -1
#             find_num(y + dy[i], x + dx[i], cnt + 1, str + '({},{})'.format(y + dy[i], x + dx[i]))
#             return
#
#     # case [2] x + 1: 우측 이동
#     if y == 0 and x + 1 < 10000:
#         MAP[y][x + 1] = -1
#         find_num(y, x + 1, cnt + 1, str + '({},{})'.format(y, x + 1))
#         return
#
#     # case [3] y + 1: 아래 이동
#     elif x == 0 and y + 1 < 10000:
#         MAP[y + 1][x] = -1
#         find_num(y + 1, x, cnt + 1, str + '({},{})'.format(y + 1, x))
#         return
#
#     return
#
#
#
#
# arr = [[0 for _ in range(10000)] for t in range(10000)]
# MAP = [[0 for _ in range(10000)] for t in range(10000)]
#
# for y in range(10000):
#     for x in range(10000):
#         arr[y][x] = '{}/{}'.format(y+1, x+1)
#
# N = int(input())
# cnt = 1
# str = '(0,0)'
# MAP[0][0] = -1
# find_num(0, 0, cnt, str)
#
# # DFS로 풀었더니
# # 시간초과 난다.
#
# # 그래서 다른 분들의 풀이를 찾아봤더니 완전 쉽게 푸는 방법이 있었다..!
# # (https://hongcoding.tistory.com/33)
# # 라인이 짝수인지/홀수인지로 방향을 결정해서 푸는 방식이었다.
#
# N = int(input())
# line = 0
# end = 0
#
# # line이 1일때 숫자 1개, line이 2일때 숫자 2개 이런 식으로 늘어나므로
# while N > end:
#     line += 1
#     end += line
#
# # N = 14일 때 end(라인의 끝값) = 15가 나온다.
# # end와 N의 차이는 1이다.
# # end 안의 분수는 line이 짝수일 경우 'line/1'이 나올 것이고, line이 홀수일 경우 '1/line'이 나온다.
# # line이 짝수일 때 end로 갈 수록 분자는 +1, 분모는 -1 된다.
# # line이 홀수일 때 end로 갈 수록 분자는 -1, 분모는 +1 된다.
#
# diff = end - N
# if line % 2 == 0:
#     top = line - diff
#     bottom = 1 + diff
# else:
#     top = 1 + diff
#     bottom = line - diff
#
# print('{}/{}'.format(top, bottom))

# # 2869 달팽이는 올라가고 싶다
#
# A, B, V = map(int, input().split())
#
# H = 0
# date = 1
#
# while H < V:
#     H += A
#     if H >= V:
#         break
#     H -= B
#     date += 1
#
# print(date)
# # 시간 초과가 나왔다.
# import math
# A, B, V = map(int, input().split())
#
# H = 0
# date = 0
# if A >= V:
#     date = 1
# elif (A - B) >= (V - A):
#     date = 2
# else:
#     tmp = (V - A) / (A - B)
#     date = math.ceil(tmp) + 1
#
# print(date)

# # 10250 ACM호텔
#
# T = int(input())
#
# for tc in range(1, T+1):
#     H, W, N = map(int, input().split())
#     cnt = 1
#     flag = False
#
#     for w in range(1, W+1):
#         for h in range(1, H+1):
#             if cnt == N:
#                 print(h*100 + w)
#                 flag = True
#                 break
#             else:
#                 cnt += 1
#         if cnt == N and flag == True:
#             break

# # 2775 부녀회장이 될테야
# # 이 문제는 n과 k가 1부터 14 사이의 작은 수여서
# # O(n제곱)의 시간복잡도가 나오더라도 이중 반복문을 사용해 풀었다.
#
# T = int(input())
#
# for tc in range(1, T+1):
#     k = int(input())
#     n = int(input())
#
#     house = [[0 for _ in range(n+1)] for z in range(k+1)]
#
#     # 0층의 room들은 1, 2, 3 순으로 사람이 들어가 있다.
#     for r in range(n+1):
#         house[0][r] = r
#
#     # k층 n호실에 사는 사람 수 = k-1층 1호실~n호실까지의 사람 수이므로
#     # 이중 반복문을 이용한다.
#     for floor in range(1, k+1):
#         for room in range(1, n+1):
#             house[floor][room] = sum(house[floor-1][0:room+1])
#
#     print(house[k][n])

# # 2839 설탕 배달
# N = int(input())
# min_num = 10000
#
# # 나누어 떨어지는 경우
# if N % 3 == 0 and N / 3 < min_num:
#     min_num = int(N / 3)
#
# if N % 5 == 0 and N / 5 < min_num:
#     min_num = int(N / 5)
#
# # 나누어 안 떨어지는데 나머지가 다른 수의 배수일 경우.
# for i in range(1, int(N/5)):
#     ret = N - (5 * i)
#     if ret % 3 == 0 and i + int(ret / 3) < min_num:
#         min_num = i + int(ret / 3)
#
# for z in range(1, int(N/3)):
#     ret = N - (3 * z)
#     if ret % 5 == 0 and z + int(ret / 5) < min_num:
#         min_num = z + int(ret / 5)
#
# if min_num == 10000:
#     min_num = -1
#
# print(min_num)

# 10757 큰 수 A+B
A, B = map(int, input().split())
print(A+B)