# # 4963 섬의 개수
# # BFS로 8방향(상하좌우대각선) 연결된 섬 찾기 176ms
# def BFS(start):
#     q = queue.Queue()
#     q.put(start)
#     i, j = start
#     visited[i][j] = 1
#
#     dx = [0, 0, 1, -1, -1, 1, -1, 1]
#     dy = [1, -1, 0, 0, -1, 1, 1, -1]
#
#     while not q.empty():
#         y, x = q.get()
#         # print(q, y, x)   #디버깅용
#         for d in range(8):
#             ny = y + dy[d]
#             nx = x + dx[d]
#             if ny < 0 or ny >= M or nx < 0 or nx >= N: continue
#             if visited[ny][nx] == 1 or MAP[ny][nx] == 0: continue
#             visited[ny][nx] = 1
#             q.put((ny, nx))
#     return
#
#     # 입력
#
#
# import sys
# import queue
# input = lambda: sys.stdin.readline().rstrip()
#
# while True:
#     N, M = map(int, input().split())
#     if N == 0 or M == 0:
#         break
#     MAP = [list(map(int, input().split())) for _ in range(M)]
#     visited = [[0 for _ in range(N)] for z in range(M)]
#
#     cnt = 0
#     for y in range(M):
#         for x in range(N):
#             if MAP[y][x] == 1 and visited[y][x] == 0:
#                 BFS((y, x))
#                 cnt += 1
#     print(cnt)

# 1926 그림 2092ms
import sys
import queue
input = lambda : sys.stdin.readline().rstrip()
# 그림 개수: 상하좌우로 연결된 것만 count
# 그림 넓이 : bfs 돌릴 때마다 sum을 return하도록 한다.
def BFS(start, sum):
    q = queue.Queue()
    q.put(start)
    y, x = start
    visited[y][x] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while not q.empty():
        y, x = q.get()
        sum += 1
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= N or nx < 0 or nx >= M : continue
            if MAP[ny][nx] == 0 or visited[ny][nx] == 1 : continue
            visited[ny][nx] = 1
            q.put((ny, nx))

    return sum

# 입력
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for z in range(N)]
# BFS
picture_cnt = 0
max_num = 0
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 1 and visited[y][x] == 0:
            ret = BFS((y, x), 0)
            max_num = max(max_num, ret)
            picture_cnt += 1

print(picture_cnt)
print(max_num)

