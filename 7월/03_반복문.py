# # 1330 두 수 비교하기
# A, B = map(int, input().split())
#
# if A > B:
#     print('>')
# elif A == B:
#     print('==')
# else:
#     print('<')
#
# # 9498 시험 성적
# n = int(input())
#
# if n >= 90 and n <= 100 :
#     print('A')
# elif n >= 80 and n < 90 :
#     print('B')
# elif n >= 70 and n < 80 :
#     print('C')
# elif n >= 60 and n < 70 :
#     print('D')
# else:
#     print('F')
#
# # 2753 윤년
# year = int(input())
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(1)
# else:
#     print(0)
#
# # 14681 사분면 고르기
#
# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)
#
# # 2884 알람 시계
#
# H, M = map(int, input().split())
#
# minute = M - 45
# hour = H
#
# if minute < 0:
#     minute = 60 + minute
#     hour = H - 1
#     if hour < 0:
#         hour = 24 + hour
#
# print('{} {}'.format(hour, minute))

# # 2525 오븐 시계
#
# H, M = map(int, input().split())
# add_M = int(input())
#
# M += add_M
#
# while M >= 60:
#     M = M - 60
#     H += 1
#     if H > 23:
#         H = 24 - H
#
# print('{} {}'.format(H, M))

# 2480 주사위 세개

a, b, c = map(int, input().split())
max_num = 0

# case 1 세개 같은 것 나오면 10000+(같은눈)*1000원
if a == b and b == c:
    print(10000 + a*1000 )
# case 2 같은 눈 2개만 나오면 1000 + 같은 눈 * 100
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
# case 3 다 다르다면 그 중 가장 큰 눈 * 100
else:
    max_num = a
    if max_num < b:
        max_num = b
    if max_num < c:
        max_num = c
    print(max_num * 100)