# 15552 빠른 A+B
import sys
read = lambda: sys.stdin.readline().rstrip()

T = int(read())
for tc in range(1, T+1):
    N, M = map(int, read().split())
    print(N + M)