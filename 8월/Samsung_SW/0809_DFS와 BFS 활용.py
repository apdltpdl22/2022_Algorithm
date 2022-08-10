# DFS가 사용되는 방식
# 1. 연결된 그래프를 모두 탐색하는 데 사용
# 2. 특정 조합을 뽑는 경우에 사용.
# 3. 순열과 조합 구현 시 많이 사용.

# BFS가 사용되는 방식
# 1. 연결된 그래프를 모두 탐색하는 데 사용
# 2. 특정 그래프에서 가중치가 모두 같을 경우 최단거리를 찾을 수 있다.

# BFS 이용 최단거리 예시 문제
# 2178 미로 164ms
import queue
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

chk = [[False for _ in range(M)] for z in range(N)]
numbers = [[1 for _ in range(M)] for z in range(N)]

def BFS(start):
    q = queue.Queue()
    q.put(start)
    y, x = start
    chk[y][x] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    numbers[y][x] = 1

    while not q.empty():
        y, x = q.get()
        # print(y, x)     # 디버깅용
        if y == N-1 and x == M-1:
            print(numbers[y][x])
            break
        for d in range(4):
            ny = dy[d] + y
            nx = dx[d] + x
            if ny >= 0 and nx >= 0 and ny < N and nx < M:
                if not chk[ny][nx] and arr[ny][nx] != 0:
                    chk[ny][nx] = True
                    numbers[ny][nx] = numbers[y][x] + 1
                    q.put((ny, nx))

BFS((0,0))
# DFS로 최단거리 구하기 왜 안될까?
# 동일 레벨인지 판단을 할 수가 없다.

# 15686 치킨배달(삼성기출) 1088ms
# 코드가 길어지니 확실히 풀다가 지친다.. 좀 줄일 필요 있음.
import sys
input = lambda : sys.stdin.readline().rstrip()

def Combination(depth, r, begin_with, arr, result):
    global combs

    if depth == r:
        combs.append(result[:])
        return

    for i in range(begin_with, len(arr)):
        result[depth] = arr[i]
        Combination(depth+1, r, i+1, arr, result)




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken_houses = []
houses = []

# 1. arr 상에 2가 위치한 좌표를 배열에 넣어, 이를 DFS를 이용해 M개씩 묶인 조합을 만든다.
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            houses.append((y,x))
        if arr[y][x] == 2:
            chicken_houses.append((y,x))
# print(chicken_houses)

combs = []
result = [0 for _ in range(M)]
if M != len(chicken_houses):
    Combination(0, M, 0, chicken_houses, result)
    # print(combs)

    min_village_score = 12000000
    min_village_combs = 0

    # 2. 조합을 이용해 새로운 MAP을 만든다.
    for i in range(len(combs)):
        MAP = arr[:]
        for y in range(N):
            for x in range(N):
                if MAP[y][x] == 2 and (y, x) not in combs[i]:
                    MAP[y][x] = 0

        # 3. 이 MAP을 이용해 각 집의 치킨 거리와 그 치킨 거리의 합들을 구한다.
        sum_chicken_score = 0
        for house in houses:
            chicken_dist = 0
            dists = []
            for chicken in combs[i]:
                dists.append(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
            chicken_dist = min(dists)
            sum_chicken_score += chicken_dist

        # 4. 치킨 거리 합들 중 최소값을 구한다.
        if sum_chicken_score < min_village_score:
            min_village_score = sum_chicken_score
            min_village_combs = combs[i]

    print(min_village_score)

# 만약 M과 arr 상의 치킨집 수가 같다면 굳이 조합을 만들 필요 없으니 그대로 계산한다.
else:
    sum_chicken_score = 0

    for house in houses:
        chicken_dist = 0
        dists = []
        for chicken in chicken_houses:
            dists.append(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        chicken_dist = min(dists)
        sum_chicken_score += chicken_dist

    print(sum_chicken_score)

# 15686 치킨배달(삼성기출) 정답 520ms
# 입력
from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chicken = [[i, j] for i in range(n) for j in range(n) if a[i][j] == 2]
home = [[i, j] for i in range(n) for j in range(n) if a[i][j] == 1]

# itertools 모듈 사용(나는 dfs로 조합 구함)
chi_list = list(combinations(chicken, m))

# 집과 치킨집 중 가장 짧은 거리 계산
def calc_dist(ho, chicken_list):
    min_dist = 1e9 #가장 큰 수
    for chi in chicken_list:
        dist = abs(chi[0] - ho[0]) + abs(chi[1] - ho[1])
        min_dist = min(min_dist, dist)
    return min_dist

ans = []
for chi in chi_list:
    total = 0
    for h in home:
        total += calc_dist(h, chi)
    ans.append(total)

print(min(ans))