# # 1978 소수 찾기
# N = int(input())
# arr = list(map(int, input().split()))
# cnt = 0
#
# for a in arr:
#     flag = False
#     if a == 1:
#         continue
#     for i in range(2, a):
#         if a % i == 0:
#             flag = True
#             break
#     if flag is True:
#         continue
#     else:
#         cnt += 1
#
# print(cnt)

# # 2581 소수
#
# M = int(input())
# N = int(input())
# arr = []
#
# for num in range(M, N+1):
#     flag = False
#     if num == 1:
#         continue
#     for i in range(2, num):
#         if num % i == 0:
#             flag = True
#             break
#
#     if flag is True:
#         continue
#     else:
#         arr.append(num)
#
# if len(arr) != 0:
#     print(sum(arr))
#     print(min(arr))
# else:
#     print(-1)

# # 11653 소인수분해 2192ms 나옴(시간 줄일 방법 연구)
#
# N = int(input())
# cnt = 0
# while N > 1:
#     for num in range(2, N+1):
#         flag = False
#         if N % num == 0:
#             for z in range(2, num):
#                 if num % z == 0:
#                     flag = True
#                     break
#         else:
#             continue
#
#         if flag is True:
#             continue
#         else:
#             print(num)
#             N = N // num
#             break

# # 1929 소수 구하기 3564ms
# # 어떤 수의 제곱근 이하까지만 소수인지 검사하면 제곱근 이상은 검사할 필요가 없다.
# import math
#
# def isPrime(m, n):
#     for num in range(m, n + 1):
#         if num == 1:
#             pass
#
#         else:
#             sq = math.sqrt(num)
#             flag = False
#             for i in range(2, int(sq)+1):
#                 if num % i == 0:
#                     flag = True
#                     break
#
#             if flag is True:
#                 continue
#             else:
#                 print(num)
#
# M, N = map(int,input().split())
# isPrime(M, N)

# import sys
# import math
#
# def isPrime(num):
#     if num == 1:
#         return
#
#     sq = int(math.sqrt(num))
#     for i in range(2, sq+1):
#         if num % i == 0:
#             return
#     print(num)
#
#     return
#
# input = sys.stdin.readline
# M, N = map(int, input().split())
#
# for num in range(M, N + 1):
#     isPrime(num)


# 4948 베르트랑 공준 1628ms
# import math
#
# def isPrime(n):
#     cnt = 0
#     for num in range(n + 1, 2 * n + 1):
#         sq = int(math.sqrt(num))
#         flag = False
#         for i in range(2, sq+1):
#             if num % i == 0:
#                 flag = True
#                 break
#
#         if flag is True:
#             continue
#         else:
#             cnt += 1
#     return cnt
#
# arr = []
# while True:
#     N = int(input())
#     if N == 0:
#         break
#     arr.append(N)
#
# for n in arr:
#     if n == 0:
#         break
#     else:
#         print(isPrime(n))

# 미리 소수인지 여부 넣어두기
max_num = 123456 * 2 + 1
num_list = [False for _ in range(123456 * 2 + 1)]

for i in range(2, max_num):
    flag = False
    sq = int(i ** 0.5)
    for z in range(2, sq + 1):
        if i % z == 0:
            flag = True
            break

    if not flag:
        num_list[i] = True

# 숫자 받아서 해당 숫자 초과, 2배 이하인 범위의
# True인 숫자 cnt 세기
arr = []

while True:
    N = int(input())
    if N == 0:
        break
    arr.append(N)

for a in arr:
    cnt = 0
    for b in range(a+1, 2*a+1):
        if num_list[b]:
            cnt += 1
    print(cnt)