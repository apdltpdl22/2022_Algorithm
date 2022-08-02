# 2447. 별 찍기 - 10 2792ms https://mgyo.tistory.com/183 참고

def recursion(N):
    global map
    if N == 3:
        map[0][:3] = map[2][:3] = [1, 1, 1]
        map[1][:3] = [1, 0, 1]
        return
    else:
        a = N // 3
        recursion(N // 3)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                for k in range(a):
                    map[a * i + k][a * j: a * (j + 1)] = map[k][:a]

        return

N = int(input())
map = [[0 for _ in range(N)] for z in range(N)]
recursion(N)
for y in range(N):
    for x in range(N):
        if map[y][x] == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# # 11729 하노이탑
# # Hanoi(n)은 H(n-1) * 2 (마지막 원반 옮기기 전, 후) + 1(마지막 원반 옮기기) 인 재귀식이다!
#
# def Hanoi(N, start, end, sub):
#

