# # 오름차순 정렬하기
# # a 자체를 변환시키는 방법
# a = [1, 5, 7, 4, 6]
# a.sort()
# print(a)
# # 출력: [1, 4, 5, 6, 7]
#
# # a를 변경하지 않고 반환값으로 저영해 넘겨주는 방식
# a = [1, 5, 7, 4, 6]
# b = sorted(a)
# print(a, b)
# # 출력:[1, 5, 7, 4, 6] [1, 4, 5, 6, 7]

# # 내림차순 정렬
# a = [1, 5, 7, 4, 6]
# a.sort(reverse = True)
# print(a)

# # 2750 수 정렬하기
# T = int(input())
# arr = list(int(input()) for _ in range(T))
# arr.sort()
# for i in arr:
#     print(i)

# # 3. 정렬 기준 정하기
# # 만약 (3,2), (5,4), (5,7) 같은 형태의 x,y꼴 좌표가 있을 때
# # 보통 sort 함수를 사용하게 되면
# # 1. x좌표를 오름차순으로,
# # 2. x좌표가 같다면 y좌표를 오름차순으로 한다.
# # 만일 y좌표만 정렬의 기준으로 하고 싶다면?
#
# a = [list(map(int, input().split())) for _ in range(5)]
# a.sort(key = lambda x:x[1])
# print(a)

# 람다를 잘 몰라서 간단하게 람다 요약
# lambda 매개변수: 표현식

# # 만약 y좌표를 오름차순으로
# # y좌표가 같다면 x좌표를 내림차순으로
# a = [list(map(int, input().split())) for _ in range(5)]
# a.sort(key=lambda x:(x[1], -x[0]))
# print(a)

# 10825 국영수
T = int(input())
for tc in range(1, T+1):
    a, *b = input().split()
    b = list(map(int, b))
    b.sort(key=lambda x: (-x[0], x[1], -x[2]))
    if b[0] == b[1] and b[1] == b[2]:

