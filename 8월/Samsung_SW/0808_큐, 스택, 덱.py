# 큐
# 먼저 들어온 데이터가 먼저 나가는 자료 구조(FIFO)

# 큐에서 주로 사용하는 연산 4가지
# 1. push : 큐의 가장 마지막에 데이터를 넣음
# 2. pop: 큐의 가장 앞의 데이터를 제거함.
# 3. front : 큐의 가장 앞의 값을 확인하는 연산
# 4. empty: 큐가 비어있는지 확인하는 연산

# 큐를 구현하기 위해 파이썬 모듈을 사용하면 된다.
# import queue / q = queue.Queue() / q.get()은 pop()처럼 출력+return이다.
# 이를 활용해 10845번 문제를 풀어보자 144ms
# import sys
# import queue
# input = lambda : sys.stdin.readline().rstrip()
# q = queue.Queue()
# n = int(input())
#
# for _ in range(n):
#     com, *num = input().split()
#
#     if com == 'push':
#         q.put(int(num[0]))
#     elif com == 'pop':
#         print(q.get() if not q.empty() else -1)
#     elif com == 'size':
#         print(q.qsize())
#     elif com == 'empty':
#         print(int(q.empty()))
#     elif com == 'front':
#         print(q.queue[0] if not q.empty() else -1)
#     elif com == 'back':
#         print(q.queue[-1] if not q.empty() else -1)

# 스택
# 나중에 들어온 게 먼저 나간다(LIFO)

# 스택 주로 사용하는 연산은 다음과 같다
# push : 스택의 가장 마지막에 데이터 넣는 연산
# pop : 스택의 가장 마지막의 데이터 제거하는 연산
# top : 스택의 가장 마지막 값을 확인하는 연산
# empty : 스택이 비어있는지 확인하는 연산
# size : 스택의 크기를 확인하는 연산

# 스택은 모듈이 없다.
# 파이썬 리스트를 사용해 만든다.
# 리스트 연산에는 다음의 함수 존재한다.
# append(x): 가장 마지막에 x추가 / pop() : 가장 마지막 원소 제거.
# 이를 이용해 10828 문제를 풀자 80ms
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# stack = []
# n = int(input())
# for _ in range(n):
#     # 뒤에 num 올수 있고 안올 수 있으므로 가변 리스트로 입력받음.
#     com, *num = input().split()
#     # 명령어에 따라 분기를 나눠줌.
#     if com == 'push':
#         stack.append(int(num[0]))
#     elif com == 'pop':
#         print(stack.pop() if not len(stack) == 0 else -1)
#     elif com == 'size':
#         print(len(stack))
#     elif com == 'empty':
#         print(int(len(stack) == 0))
#     elif com == 'top':
#         print(stack[-1] if not len(stack) == 0 else -1)

# 덱(deque)
# 양방향 큐: 양방향 모두 삽입 삭제 가능
# 덱 함수들
# append(x) : 덱의 가장 뒤에 x 삽입
# appendleft(x): 덱의 가장 앞에 x 삽입
# pop(): 덱의 가장 마지막 원소 제거하며 반환
# popleft() : 덱의 가장 처음 원소 제거하며 반환

# 덱 선언
# from collections import deque
# dq = deque()
# 10866 문제를 풀어보자 104ms

# from collections import deque
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# dq = deque()
# n = int(input())
#
# for _ in range(n):
#     com, *num = input().split()
#
#     if com == 'push_front':
#         dq.appendleft(int(num[0]))
#     elif com == 'push_back':
#         dq.append(int(num[0]))
#     elif com == 'pop_front':
#         print(dq.popleft() if not len(dq) == 0 else -1)
#     elif com == 'pop_back':
#         print(dq.pop() if not len(dq) == 0 else -1)
#     elif com == 'size':
#         print(len(dq))
#     elif com == 'empty':
#         print(int(len(dq) == 0))
#     elif com == 'front':
#         print(dq[0] if not len(dq) == 0 else -1)
#     elif com == 'back':
#         print(dq[-1] if not len(dq) == 0 else -1)