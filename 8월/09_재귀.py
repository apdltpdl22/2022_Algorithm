# 10872 팩토리얼
# 첫 번째 방법: 재귀함수
def fact(N):
    if N > 0:
        return N * fact(N-1)
    else:
        return 1

N = int(input())
ret = fact(N)
print(ret)

# 두 번째 방법 : 반복문 활용
N = int(input())
sum = 1
for i in range(N, 0, -1):
    sum *= i
print(sum)

# 세 번째 방법: math.factorial() 함수 활용 72ms로 이게 제일 시간 오래 걸림.
import math
N = int(input())
print(math.factorial(N))

# 10870 피보나치 수 5
# DP를 배우면 이미 배열에 값이 저장된 애는 패스하는 방법으로 시간을 단축할 수 있겠지.
def Fibo(N):
    if N > 2:
        arr[N] = Fibo(N-1) + Fibo(N-2)
    elif N > 0:
        arr[N] = 1
    else:
        arr[N] = 0

    return arr[N]

N = int(input())
arr = [0 for _ in range(N+1)]
ret = Fibo(N)
print(ret)

#17478 재귀함수가 뭔가요?
def recursion(N, lines):
    print(lines + '\"재귀함수가 뭔가요?\"')
    if N > 0:
        print(lines + '\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(lines + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(lines + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"')
        recursion(N-1, lines+'____')
    else:
        print(lines+'\"재귀함수는 자기 자신을 호출하는 함수라네\"')

    print(lines+'라고 답변하였지.')
    return

N = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
lines = ''
recursion(N, lines)


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

# 11729 하노이탑 924ms
# https://mgyo.tistory.com/185 참고
# Hanoi(n)은 H(n-1) * 2 (마지막 원반 옮기기 전, 후) + 1(마지막 원반 옮기기) 인 재귀식이다!

MSG_FORMAT = '{} {}'
def Move(start, end):
    print(MSG_FORMAT.format(start, end))

def Hanoi(N, start, end, sub):
    if N == 1:
        Move(start, end)
        return
    else:
        Hanoi(N-1, start, sub, end)
        Move(start, end)
        Hanoi(N-1, sub, end, start)

N = int(input())
print(2 ** N - 1)
Hanoi(N, 1, 3, 2)