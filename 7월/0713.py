# # 2739 구구단
#
# N = int(input())
#
# for i in range(1, 10):
#     if i == 9:
#         print('{} * {} = {}'.format(N, i, N * i), end='')
#     else:
#         print('{} * {} = {}'.format(N, i, N*i))
#
#
# # 10950 A+B-3
# T = int(input())
# arr = []
#
# for test in range(1, T+1):
#     n, m = map(int, input().split())
#     arr.append(n+m)
#
# for i in range(len(arr)):
#     if i == len(arr) - 1:
#         print(arr[i], end='')
#     else:
#         print(arr[i])
#
# # 8393 합
# n = int(input())
# sum = 0
# # 1. 그냥 반복문으로 다 더한다.
# for i in range(1, n+1):
#     sum += i
# print(sum)
#
# # 2. 수학 공식을 이용한다.
# sum = n*(n+1) // 2
# print(sum)


# # 15552 빠른 A+B
#
# import sys
#
# T = int(input())
#
# for tc in range(1, T+1):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     print(a+b)
#
#
# # 2742 기찍 N
# N = int(input())
#
# for i in range(N, 0, -1):
#     if i == 1:
#         print(i, end='')
#         break
#     print(i)
#
#
# # 11021 A+B-7
# import sys
#
# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, sys.stdin.readline().rstrip().split())
#     print('Case #{}: {}'.format(tc, n+m))
#
#
# # 2438 별 찍기 - 1
# N = int(input())
#
# for i in range(1, N+1):
#     if i == N:
#         print('*' * i, end='')
#         break
#     print('*' * i)
#

# 2439 별 찍기 - 2
N = int(input())

for i in range(1, N+1):
    if i == N:
        print(' ' * (N-i) + '*' * i, end='')
        break
    print(' ' * (N-i) + '*' * i)