# # DFS-BFS는 그래프를 모두 탐색에 사용하는 알고리즘
# # 1. BFS
# # BFS 구현에는 큐가 필요함.
#
# # 그래프의 표현 방식에는 두가지가 있다.
# # 1. 인접 행렬 방식
# # 1번과 2번 노드가 이어져있다면 arr[1][2]와 arr[2][1]에
# # true 혹은 1을 입력한다.
# n, m, v = map(int, input().split()) #정점의 개수, 간선의 개수, 시작 번호
# a = [[0] * (n+1) for _ in range(n+1)]
# for _ in range(m):
#     x, y = map(int, input().split())
#     a[x][y] = 1
#     a[y][x] = 1
#
# for x in a:
#     print(x)
#
# # 양방향 리스트라는 조건이 있을 때 보통 이런 식으로 한다.
# # 하지만 1번 노드와 연결된 다른 노드들을 알기 위해
# # 2번부터 n번까지 모두 뒤져야 해서 비효율적이다.
# # 그래서 아래처럼 인접 리스트 방식이 좀 더 효율적이다.
#
# n, m, v = map(int, input().split()) #정점의 개수, 간선의 개수, 시작번호
# a = [list() for _ in range(n+1)]
# for _ in range(m):
#     x, y = map(int, input().split())
#     a[x].append(y)
#     a[y].append(x)
#
# # 정점 번호가 작은 순으로 탐색해야 할 경우
# for x in a:
#     x.sort()
#
# for x in a:
#     print(x)
#
# # 2. DFS
# # 보통 DFS와 BFS의 탐색 순서는 다르다.
# # DFS에도 체크 배열(visited 배열)은 필요하다. 이미 방문한 곳을 중복방문하는 것을 피하기 위해서이다.

# 1260 DFS와 BFS 696ms
import queue
n, m, v = map(int, input().split())
# 빈 그래프 리스트 만들기
a = [list() for _ in range(n+1)]
# 간선 연결(인접리스트 방식)
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for x in a:
    x.sort()
# BFS 함수 구현
def BFS(start):
    q = queue.Queue()
    # 시작 노드를 큐에 미리 넣어둠.
    q.put(v)
    # 이 체크는 큐에서 방문하기 전!!에
    # 방문할 노드 번호를 미리 체크하는 것이다.
    chk[v] = True

    while not q.empty():
        now = q.get()               # 큐에서 가장 앞의 노드를 꺼내온다.
        print(now, end=' ')         # 해당 노드를 방문한다는 의미로 출력한다.
        for next in a[now]:         # 방문한 노드의 인접 노드들을 for문을 통해 next에 저장
            if not chk[next]:       # 인접 노드가 이미 방문된 상태가 아닐 때만
                chk[next] = True    # 체크를 해주고,
                q.put(next)         # 인접 노드를 큐에 넣어준다.
    print()

# DFS 함수 구현
def DFS(now):
    # 맨 처음 시작노드부터 chk를 True로 놓을 수 있도록.
    chk[now] = True     # 미리 큐에 넣는 BFS와 달리 재귀적으로 다음 노드로 넘어가는 BFS라 이미 넘어간 다음 chk에 체크하는 것이 가능하다.
    print(now, end=' ')

    for next in a[now]:
        if not chk[next]:
            DFS(next)

chk = [False] * (n+1)
DFS(v)
print()
chk = [False] * (n+1)
BFS(v)