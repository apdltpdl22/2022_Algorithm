# # 2798 블랙잭
# # 정말 모든 경우를 다 구하는 완전 탐색 방식.
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr = sorted(arr)
#
# ret = 0
# for i in range(N):
#     for j in range(N):
#         for z in range(N):
#             if i != j and j != z and i != z:
#                 if arr[i] + arr[j] + arr[z] > M:continue
#                 else:
#                     ret = max(ret, arr[i] + arr[j] + arr[z])
# print(ret)

# # 2231 분해합 1276ms
# # 파이썬 함수 사용해서 좀 치사하게 푼 것 같은 느낌..
# # 나중에 JS로 코테 준비하게 되면 다시 풀어봐야 할 것 같다.
#
# N = int(input())
# arr = []
#
# for i in range(N+1):
#     if i + sum(map(int, str(i)[::])) == N:
#         arr.append(i)
#
# if len(arr) != 0:
#     print(min(arr))
# else:
#     print(0)

# # 7568 덩치 (처음에 키나 몸무게 같은 상태에서 둘 중 하나가 우수한 쪽이 덩치가 더 크다고 생각했는데 문제에선 둘 다 커야만 덩치가 크다였음)
# N = int(input())
# arr = []
# cnt_arr = [0 for _ in range(N)]
# rank = [0 for _ in range(N)]
#
# for n in range(N):
#     x, y = map(int, input().split())
#     arr.append((x, y))
#
# for a in range(N):
#     for rival in range(N):
#         if rival == a: continue
#         # 몸무게, 키 둘다 a가 a+1번째보다 클 때
#         if arr[a][0] < arr[rival][0] and arr[a][1] < arr[rival][1]:
#             cnt_arr[a] += 1
#
#         # #몸무게 같을 경우
#         # elif arr[a][0] == arr[rival][0]:
#         #     if arr[a][1] < arr[rival][1]:
#         #         cnt_arr[a] += 1
#         #
#         # #키가 같을 경우
#         # elif arr[a][1] == arr[rival][1]:
#         #     if arr[a][0] < arr[rival][0]:
#         #         cnt_arr[a] += 1
#
# for c in cnt_arr:
#     print(c + 1, end=' ')
# print()

