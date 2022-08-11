# # 15649 N과 M(1) 320ms
# def DFS(depth, chk, result):
#     if depth == M:
#         permutations.append(result[:])
#         return
#
#     for i in range(1, N+1):
#         if chk[i]: continue
#         chk[i] = True
#         result[depth] = i
#         DFS(depth+1, chk, result)
#         chk[i] = False
#
# N, M = map(int, input().split())
# chk = [False for _ in range(N+1)]
# result = [0 for _ in range(M)]
# permutations = []
# DFS(0, chk, result)
# #
# # for p in permutations:
# #     for m in range(M):
# #         print(p[m], end=' ')
# #     print()
#
# # 15654 N과 M(5)
# # DFS로 수열 구현
# import sys
# input= lambda : sys.stdin.readline().rstrip()
#
# def DFS(depth, result):
#     if depth == M:
#         # print(result) # 디버깅용
#         permutations.append(result[:])
#         return
#
#     for i in range(N):
#         if chk[i]: continue
#         chk[i] = True
#         result[depth] = arr[i]
#         DFS(depth+1, result)
#         chk[i] = False
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# result = [0 for _ in range(M)]
# chk = [False for _ in range(N)]
# permutations = []
# DFS(0, result)
#
# for p in permutations:
#     for m in range(M):
#         print(p[m], end=' ')
#     print()

# # 15655 N과 M (6) 68ms
# # 중복되지 않는 조합
# def DFS(begin, depth, result):
#     if depth == M:
#         # print(result) #디버깅용
#         combinations.append(result[:])
#         return
#
#     for i in range(begin, N):
#         result[depth] = arr[i]
#         DFS(i+1, depth+1, result)
#
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# #입력
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort() # 오름차순으로 수열 만들기 위해
#
# # DFS(중복X조합)
# result = [0 for _ in range(M)]
# combinations = []
# DFS(0, 0, result)
#
# for c in combinations:
#     for m in range(M):
#         print(c[m], end=' ')
#     print()

# # 15657 N과 M (8) #108ms
# # 중복 허용 조합 만들기 => chk 배열 필요 X
# def DFS(begin, depth, result):
#     if depth == M:
#         # print(result) #디버깅용
#         combinations.append(result[:])
#         return
#
#     for i in range(begin, N):
#         result[depth] = arr[i]
#         DFS(i, depth+1, result) # 중복가능이니 i+1부터 말고 i부터 올라가도록
#
# #입력
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
#
# # DFS
# result = [0 for _ in range(M)]
# combinations = []
# DFS(0, 0, result)
#
# for c in combinations:
#     for m in range(M):
#         print(c[m], end=' ')
#     print()

# # 15663 N과 M (9) => 백준에서는 시간초과, 184ms
# # 입력
# # 중복 허용 X, 같은 순열 허용 X 순열
# def DFS(depth, result):
#     if depth == M:
#         # print(result) # 디버깅용
#         permutations.append(result[:])
#         return
#     last = 0                        # depth 달라지면 0으로 last 초기화
#     for i in range(N):
#         if chk[i] : continue
#         if last == arr[i] : continue
#         chk[i] = True
#         last = arr[i]               # 같은 자리(depth)에 오는 애가 같지 않게 하기.
#         result[depth] = arr[i]
#         DFS(depth + 1, result)
#         chk[i] = False
#
# import sys
# input = lambda : sys.stdin.readline().rstrip()
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
#
# # DFS
# result = [0 for _ in range(M)]
# chk = [False for _ in range(N)]
# permutations = []
# DFS(0, result)
#
# for p in permutations:
#     for m in range(M):
#         print(p[m], end=' ')
#     print()

# # 15664 N과 M (10)
# def DFS(begin, depth, result):
#     if depth == M:
#         # print(result)       # 디버깅용
#         combinations.append(result[:])
#         return
#     last = 0
#     for i in range(begin, N):
#         if last == arr[i] : continue
#         last = arr[i]
#         result[depth] = arr[i]
#         DFS(i + 1, depth + 1, result)
# # 입력
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
#
# #DFS - 중복 X 조합(depth 다르면 같은 수 상관X)
# result = [0 for _ in range(M)]
# combinations = []
# DFS(0, 0, result)
#
# for c in combinations:
#     for m in range(M):
#         print(c[m], end=' ')
#     print()

# # 15665 N과 M (11) 1488ms
# def DFS(depth, result):
#     if depth == M:
#         # print(result)   # 디버깅용
#         permutations.append(result[:])
#         return
#     last = 0
#     for i in range(N):
#         if last == arr[i]: continue
#         last = arr[i]
#         result[depth] = arr[i]
#         DFS(depth+1, result)
#
# #입력
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
#
# #DFS(중복 허용하는 수열. 깊이 다르면 같은 값 ok)
# result = [0 for _ in range(M)]
# permutations = []
# DFS(0, result)
#
# for p in permutations:
#     for m in range(M):
#         print(p[m], end=' ')
#     print()

# # 15666 N과 M (12) 84ms
# def DFS(begin, depth, result):
#     if depth == M:
#         combinations.append(result[:])
#         return
#     last = 0
#     for i in range(begin, N):
#         if last == arr[i]: continue
#         last = arr[i]
#         result[depth] = arr[i]
#         DFS(i, depth+1, result) # 중복 허용하므로 i+1 대신 i
# # 입력
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
#
# # DFS(중복 허용하는 조합, depth 다르면 같은 값O)
# result = [0 for _ in range(M)]
# combinations = []
# DFS(0, 0, result)
#
# for c in combinations:
#     for m in range(M):
#         print(c[m], end=' ')
#     print()

# # 2529 부등호
# def DFS(depth, result):
#     if depth > 1:
#         if A[depth-2] == '<':
#             if not int(result[depth-2]) < int(result[depth-1]): return
#
#         elif A[depth-2] == '>':
#             if not int(result[depth-2]) > int(result[depth-1]): return
#
#     if depth == K+1:
#         permutations.append(result)
#         return
#
#     for i in range(10):
#         if chk[i] : continue
#         chk[i] = True
#         DFS(depth+1, result + str(i))
#         chk[i] = False
#
# # 입력
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# K = int(input())
# A = list(input().split())
#
# # 중복 X 순열 구하기
# result = ''
# chk = [0 for _ in range(10)]
# permutations = []
# DFS(0, result)
#
# #최대값, 최소값 구하기
# max_num = 0
# min_num = 999999999999999
#
# for p in permutations:
#     if int(p) > int(max_num):
#         max_num = p
#
#     if int(p) < int(min_num):
#         min_num = p
#
# print(max_num)
# print(min_num)

# # 14888 연산자 끼워넣기 124ms
# def DFS(depth, result, debug_str):
#     if depth == N-1:
#         results.append(result)
#         return
#
#     last = -5
#
#     for i in range(4):
#         if last == i: continue  #같은 위치(depth)에 같은 연산자 오는 것 방지
#         if not operators[i] > 0: continue # 연샨자 1개 이상 있어야 가능
#         operators[i] -= 1
#         last = i
#
#         if i == 0:              # + 연산자일 때
#             DFS(depth+1, result + A[depth+1], debug_str + '+')
#         if i == 1:              # - 연산자일 때
#             DFS(depth+1, result - A[depth+1], debug_str + '-')
#         if i == 2:              # * 연산자일 때
#             DFS(depth+1, result * A[depth+1], debug_str + '*')
#         if i == 3:              # // 연산자일 때 (정수나눗셈으로 몫만 취함)
#             if result < 0 and A[depth+1] >= 0:
#                 DFS(depth+1, -(-result // A[depth+1]), debug_str + '/')
#             else:
#                 DFS(depth+1, result // A[depth+1], debug_str + '/')
#
#         operators[i] += 1     #다시 돌아왔을 때 +1 상태 돌려놓음.
#
#
# # 입력
# import sys
# input = lambda : sys.stdin.readline().rstrip()
#
# N = int(input())
# A = list(map(int, input().split()))
# operators = list(map(int, input().split()))
#
# # 중복 허용X 순열 (연산자의 순열)
# result = A[0]
# debug_str = ''
# results = []
# DFS(0, result, debug_str)
#
# min_num = 1000000001
# max_num = -1000000001
#
# for r in results:
#     if r < min_num:
#         min_num = r
#     if r > max_num:
#         max_num = r
#
# print(max_num)
# print(min_num)

# 14889 스타트와 링크
# 중복 없는 조합의 중복 없는 수열을 구하기.  # 시간 초과 -> 재귀 2번 말고 그냥
def Combination(begin, depth, result):
    if depth == N//2:
        # result[0]에 들어가지 않은 애들을 result[1]에 넣음.
        c = 0
        for i in range(N):
            if i not in result[0]:
                result[1][c] = i
                c += 1
        combinations.append([tuple(result[0]), tuple(result[1])])
        result[1] = [0 for _ in range(N//2)]
        return

    for d in range(begin, N):
        result[0][depth] = d
        Combination(d+1, depth+1, result)

def Permutation_start(depth, tup, result):
    global sums_start
    if depth == 2:
        sums_start += arr[result[0]][result[1]]
        # print(result, sums_start)     # 디버깅용
        return

    last = -5                   # 초기화
    for num in tup:
        if last == num: continue
        last = num
        result[depth] = num
        Permutation_start(depth+1, tup, result)

def Permutation_link(depth, tup, result):
    global sums_link
    if depth == 2:
        sums_link += arr[result[0]][result[1]]
        # print(result, sums_link)     # 디버깅용
        return

    last = -5                   # 초기화
    for num in tup:
        if last == num: continue
        last = num
        result[depth] = num
        Permutation_link(depth+1, tup, result)

# 입력
import sys
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 중복 X 조합( N개 중 N//2개 선택)
combinations = []
result = [[0 for _ in range(N//2)] for z in range(2)]
Combination(0, 0, result)

# 중복 X 조합들
# 0번 튜플이 스타트, 1번 튜플이 링크라 가정할 때
# 각 튜플에서 2개씩 뽑는 중복 X 순열 모두 구하고 해당 순열들의 값들 총합 구함.
# 양 튜플의 총합을 뺀 값의 절대값을 min_num과 비교

min_num = 10000
for comb in combinations:
    result = [0, 0]
    sums_start = 0
    sums_link = 0
    Permutation_start(0, comb[0], result)
    Permutation_link(0, comb[1], result)
    min_num = min(min_num, abs(sums_start - sums_link))
    # print(min_num)

print(min_num)