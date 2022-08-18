# 4963 섬의 개수
# 입력
import sys
# import queue
input = lambda : sys.stdin.readline().rstrip()

def BFS(start):
    q = queue.Queue()
    q.put(start)
    i, j = start
    visited[i][j] = 1

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    while not q.empty():
        now = q.get()
        y, x = now
        # print(now, end= ' ')
        for d in range(4):
            ny = dy[d] + y
            nx = dx[d] + x
            if ny < 0 or ny >=M : continue
            if nx < 0 or nx >= N: continue
            visited[ny][nx] = 1
            next = (ny, nx)
            q.put(next)


while True:
    N, M = map(int, input().split())
    if N == 0 or M == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(M)]

    # BFS
    # 연결된 애들을 모두 찾는 것이니 BFS 돌리는 게 더 빠르다.
    visited = [list(0 for _ in range(N)) for _ in range(M)]
    cnt = 0   #  섬 개수
    for y in range(M):
        for x in range(N):
            if MAP[y][x] == 1 and visited[y][x] == 0:
                BFS((y,x))
                cnt += 1
    print(cnt)