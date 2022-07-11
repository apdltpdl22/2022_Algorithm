#10172 개

# print('''|\\_/|
# |q p|   /}
# ( 0 )\"\"\"\\
# |\"^\"`    |
# ||_/=\\\\__|''')

# 1000 A+B
# n, m = map(int, input().split())
# print(n + m)

# 1008 A/B
# n, m = map(int, input().split())
# print(n / m)

# 10926
# case = input()
# print("{}??!".format(case))

# 18108
# y = int(input())
#
# if y >= 1000 and y <= 3000:
#     print(y - 543)
# else:
#     print('1000과 3000 사이의 수를 입력해주세요.')


# 10430
# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print( ((A%C) * (B%C))%C)

# 2588 곱셈
n = int(input())
m = input()
sum = 0

for i in range(2, -1, -1):
    num = int(m[i]) * n
    print(num)
    sum += num * (10 ** (2-i))

print(sum)
