# # 1330
# A, B = map(int, input().split())
#
# if A > B:
#     print('>')
# elif A == B:
#     print('==')
# else:
#     print('<')

# 9498
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

# # 2753
# year = int(input())
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(1)
# else:
#     print(0)

# 14681 사분면 고르기

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

# 2884 알람 시계

H, M = map(int, input().split())

minute = M - 45
hour = H

if minute < 0:
    minute = 60 + minute
    hour = H - 1
    if hour < 0:
        hour = 24 + hour

print('{} {}'.format(hour, minute))