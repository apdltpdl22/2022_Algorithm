# 1. 순열과 조합의 개념
# 순열이란 순서를 신경쓰며 뽑는 방식
# 조합이란 순서에 상관 없이 뽑는 방식

# 2. 중복 없는 순열 구현
# 파이썬에는 순열과 조합 모듈이 있다.
# itertools 사용하면 간단(그러나 삼성에서는 허용 안하므로 DFS나 DP 사용할 듯)

# 중복 없는 순열
from itertools import permutations
# 중복 없는 조합
from itertools import combinations
# 중복 있는 순열 / 각 집단에서 추출
from itertools import product
# 중복 있는 조합
from itertools import combinations_with_replacement as com

# 예시 : 1,2,3 중 3개를 중복 없이 뽑는 순열
from itertools import permutations
print(list(permutations([1, 2, 3], 3)))

# 10974 모든 순열 268ms
from itertools import permutations
n = int(input())
arr = []
for i in range(1, n+1):
    arr.append(i)
result = (list(permutations(arr, n)))
for r in result:
    for d in range(n):
        if d == n-1:
            print(r[d])
        else:
            print(r[d], end=' ')

# 10974 모든 순열 모범답안 180ms
from itertools import permutations
n = int(input())
result = (list(permutations(range(1, n+1))))
# *r => 튜플 언패킹
for r in result:
    print(*r)

# 10819 차이를 최대로 184ms
from itertools import permutations
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
pms = list(permutations(list(map(int, input().split())), n))
max_cnt = 0
for pm in pms:
    cnt = 0
    for i in range(1, n):
        cnt += abs(pm[i-1] - pm[i])
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)

# 3. 중복 없는 조합
# 15650 N과 M(2) 72ms
import sys
from itertools import combinations
N, M = map(int, input().split())
comb = (list(combinations(range(1, N+1), M)))
for c in comb:
    print(*c)

# 6603 로또 72ms
import sys
from itertools import combinations
while True:
    k, *S = map(int, input().split())
    if k == 0:
        break
    comb = list(combinations(S, 6))
    for c in comb:
        print(*c)
    print()
# 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 716ms
import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
all_comb = list(combinations(range(1, N+1), 3))
no_mat = [[0 for _ in range(N+1)] for z in range(N+1)]
for _ in range(M):
    y, x = map(int, input().split())
    no_mat[y][x] = 1
    no_mat[x][y] = 1
cnt = 0
for c in all_comb:
    if no_mat[c[0]][c[1]] or no_mat[c[1]][c[2]] or no_mat[c[2]][c[0]]:
        continue
    cnt += 1
print(cnt)

# 4. 중복 있는 순열 / 각 집단에서 추출 구현
# from itertools import product

# 15651 N과 M(3) 2060ms
import sys
from itertools import product
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
ret = list(product(range(1, N+1), repeat=M))
for r in ret:
    print(*r)

# 15656 N과 M(7) 2496ms
import sys
from itertools import product
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ret = list(product(arr, repeat=M))
for r in sorted(ret):
    print(*r)

# 5. 중복 있는 조합
# from itertools import combinations_with_replacement as combr

# 15652 N과 M (4) 88ms
# 비내림차순 => (1,4)는 되고 (4,1)은 안됨 => 중복 허용 조합
from itertools import combinations_with_replacement as combr
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
arr = list(combr(range(1, N+1), M))
for a in arr:
    print(*a)