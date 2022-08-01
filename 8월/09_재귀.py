# 10872 팩토리얼
# 첫 번째 방법: 재귀함수
# def fact(N):
#     if N > 0:
#         return N * fact(N-1)
#     else:
#         return 1
#
# N = int(input())
# ret = fact(N)
# print(ret)

# # 두 번째 방법 : 반복문 활용
# N = int(input())
# sum = 1
# for i in range(N, 0, -1):
#     sum *= i
# print(sum)

# # 세 번째 방법: math.factorial() 함수 활용 72ms로 이게 제일 시간 오래 걸림.
# import math
# N = int(input())
# print(math.factorial(N))

# 10870 피보나치 수 5
# DP를 배우면 이미 배열에 값이 저장된 애는 패스하는 방법으로 시간을 단축할 수 있겠지.
# def Fibo(N):
#     if N > 2:
#         arr[N] = Fibo(N-1) + Fibo(N-2)
#     elif N > 0:
#         arr[N] = 1
#     else:
#         arr[N] = 0
#
#     return arr[N]
#
# N = int(input())
# arr = [0 for _ in range(N+1)]
# ret = Fibo(N)
# print(ret)

# def recursion(N):
#     if N == 0:
#         pass
#
# N = int(input())
# print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')