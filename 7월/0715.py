# # 10818 최소, 최대
# import sys
#
# N = int(input())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
#
# # 처음부터 다 찾는 방법(476ms)
# min_num = 10000001
# max_num = -2000000
#
# for i in arr:
#     if i > max_num:
#         max_num = i
#
#     if i < min_num:
#         min_num = i
#
# print('{} {}'.format(min_num, max_num))
#
# # 더 빠른 방법은 없을까?
# # 1. 절반으로 나눠서 min, max 각각 찾고 두 종류 비교하면? - 이게 더 시간 걸린다.(576ms)
#
# import sys
#
# N = int(input())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
#
# # 처음부터 다 찾는 방법
# min_num_1 = min_num_2 = 10000001
# max_num_1 = max_num_2 = -2000000
#
# for i in range(0, N//2):
#     if arr[i] > max_num_1:
#         max_num_1 = arr[i]
#
#     if arr[i] < min_num_1:
#         min_num_1 = arr[i]
#
# for i in range(N//2, N):
#     if arr[i] > max_num_2:
#         max_num_2 = arr[i]
#
#     if arr[i] < min_num_2:
#         min_num_2 = arr[i]
#
# if min_num_1 <= min_num_2:
#     min_num = min_num_1
# else:
#     min_num = min_num_2
#
# if max_num_1 >= max_num_2:
#     max_num = max_num_1
# else:
#     max_num = max_num_2
#
# print('{} {}'.format(min_num, max_num))
#
# # 2. max, min 쓴다면? - 아까보다 빨라졌음.(424ms)
# import sys
#
# N = int(input())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
#
# print('{} {}'.format(min(arr), max(arr)))


# # 2562 최댓값
#
# # 리스트에 안 넣고 푸는 방법도 있겠지만(max_num 잡아두고, while 문 돌리며 비교하고, EOFError 발생했을 때 최댓값 출력한다던지.)
# # 9개라는 고정된 숫자가 주어졌으므로 리스트에 넣는 방법으로 가보자.
#
# arr = []
# max_num = 0
# max_idx = 0
#
# for i in range(9):
#     n = int(input())
#     if n > max_num:
#         max_num = n
#         max_idx = i+1
#
# print('{}\n{}'.format(max_num, max_idx))

# # 2577 숫자의 개수
# # 문자열로 푸는 것이 더 쉬워보여 곱셈의 결과를 문자열로 치환해 풀었다.
#
# arr = []
# numbers = [0 for _ in range(10)]
#
# for i in range(3):
#     arr.append(int(input()))
#
# A, B, C = arr[0], arr[1], arr[2]
# multiply = str(A * B * C)
#
# for num in multiply:
#     numbers[int(num)] += 1
#
# for i in range(10):
#     if i == 9:
#         print(numbers[i], end='')
#         break
#     print(numbers[i])

# 3052 나머지

# arr = set()
# for i in range(10):
#     n = int(input()) % 42
#     arr.add(n)
#
# # 중복을 허용하지 않는 set을 만들어서, set의 length만 나중에 세주기.
# print(len(arr), end='')

# List만 쓴다면 위의 문제처럼 배열을 만들어서 할 수 있는데,
# 숫자를 카운트 하기 위한 배열이 42개이므로 메모리 차지 많음.

# arr = []
# numbers = [0 for _ in range(42)]
#
# for i in range(10):
#     n = int(input()) % 42
#     if numbers[n] == 0:
#         numbers[n] += 1
#
# print(sum(numbers), end='')

