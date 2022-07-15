# 10818 최소, 최대(476ms)
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 처음부터 다 찾는 방법
min_num = 10000001
max_num = -2000000

for i in arr:
    if i > max_num:
        max_num = i

    if i < min_num:
        min_num = i

print('{} {}'.format(min_num, max_num))

# 더 빠른 방법은 없을까?
# 1. 절반으로 나눠서 min, max 각각 찾고 두 종류 비교하면? - 이게 더 시간 걸린다.(576ms)

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 처음부터 다 찾는 방법
min_num_1 = min_num_2 = 10000001
max_num_1 = max_num_2 = -2000000

for i in range(0, N//2):
    if arr[i] > max_num_1:
        max_num_1 = arr[i]

    if arr[i] < min_num_1:
        min_num_1 = arr[i]

for i in range(N//2, N):
    if arr[i] > max_num_2:
        max_num_2 = arr[i]

    if arr[i] < min_num_2:
        min_num_2 = arr[i]

if min_num_1 <= min_num_2:
    min_num = min_num_1
else:
    min_num = min_num_2

if max_num_1 >= max_num_2:
    max_num = max_num_1
else:
    max_num = max_num_2

print('{} {}'.format(min_num, max_num))

# 2. max, min 쓴다면? - 아까보다 빨라졌음.(424ms)
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

print('{} {}'.format(min(arr), max(arr)))


