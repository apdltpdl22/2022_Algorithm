# # 15596 정수 n개의 합
# def solve(a):
#     ans = 0
#     for num in a:
#         ans += num
#     return ans
#
# # 4673 셀프 넘버
# # 함수 d를 정의해서 문제를 풀라 했으니, 우선 수열을 만들 수 있는 함수 d를 생성한다.
# # 문자열로 자리수를 구해서 풀 수도 있지만, 조금 더 어렵게 풀어보기 위해 로그를 이용해 자리수를 알아내는 방식을 사용해봤다.
# # 그랬더니 ValueError: math domain error가 일어난다. 확인해보니 반복문을 1이 아니라 0부터 시작하게 설정해놨었다.
# # log(0)은 정의될 수 없으므로 오류가 난다.
#
# import math
#
# def d(n):
#     result = n
#     log_num = math.log10(n)
#     zero_numbers = math.trunc(log_num)
#
#     while n > 0:
#         result += n // (10 ** zero_numbers)
#         n %= (10 ** zero_numbers)
#         zero_numbers -= 1
#
#     return result
#
#
# # d의 result가 될 수 없는 셀프 넘버를 구하는 방법을 나는 이렇게 했다.
# # d 함수에 1부터 10000까지를 다 넣어서, 결과값을 set으로 만들고,
# # 1부터 10000까지의 수 중 그 안에 없는 수를 찾는다.
#
# results = set()
# for i in range(1, 10000):
#     results.add(d(i))
#
# for i in range(1, 10000):
#     if i not in results:
#         print(i)
#
#
# # 1065 한수
# # 한수인지 판별하는 함수를 만들어 문제를 풀어보자!
# # 포인트 1. 숫자가 1개만 있는 것도 수열이 성립한다.
# # 포인트 2. 10<=n<=99 구간에서는 공차가 0인 등차수열의 존재를 생각해야 한다.
# # 포인트 3. 등차수열의 n차 항을 구하는 방법은 a(n) = a(1) + (n-1)d이다.
# # 자리수들 간에 이 관계가 성립하는지 확인하자.
#
# import math
# def check(n):
#     arr = []
#     # 자리수만 가변 리스트에 넣기
#     log_num = math.trunc(math.log10(n))
#
#     while log_num >= 0:
#         arr.append((n // (10 ** log_num)))
#         n %= (10 ** log_num)
#         log_num -= 1
#
#     # 가변 리스트에 넣은 숫자들의 공차가 일정한지 확인해본다.
#     # 먼저 arr[1] - arr[0]으로 공차(d)를 초기화하고,
#     # 반복문을 돌리며, 나머지 숫자들의 차가 d와 일치하는지 확인한다.
#     d = arr[1] - arr[0]
#     result = True
#     for z in range(len(arr) - 1, 1, -1):
#         if arr[z] - arr[z-1] != d:
#             result = False
#             break
#
#     return result
#
# N = int(input())
#
# if 0 < N and N < 10:
#     print(N)
#
# else:
#     cnt = 9
#     for i in range(10, N+1):
#         if check(i) == True:
#             cnt += 1
#     print(cnt)
#
# # 인덱스 에러가 계속 나서 왜 이러나 했는데, len(arr)을 초기값으로 지정할 때 len(arr) - 1을 안해준데다,
# # 함수 밖의 반복문 iterator로 i를 썼으면서, 함수 안의 반복문에도 i를 쓰고 있었다...! 급하게 z로 바꿔줌
# # 그리고 하나라도 틀리면 result False로 바꿔주고 바로 반복문 나가버리도록 break를 추가해줬더니
# # 매끈히 잘 동작했다!
#
# # 11654 아스키 코드
# # 파이썬에서 ASCII -> 숫자는 ord(), 숫자 -> ASCII는 chr() 함수를 사용한다!
# print(ord(input()))

# # 11720 숫자의 합
#
# N = int(input())
# word = input()
# sum = 0
#
# for i in word:
#     sum += int(i)
#
# print(sum)

# # 10809 알파벳 찾기
# # 우선 알파벳 개수 만큼 -1을 채워 넣은 리스트를 만든다.(알파벳은 26개)
# # 이렇게 하면 -1이 아닌 숫자들은 자릿수가 채워진 것이고, 한번도 등장하지 않은 알파벳의 자리수는 -1로 남아있다.
# arr = [-1 for _ in range(26)]
#
# # 아스키 코드로 a는 97, z는 122이다.
# # 그래서 word를 반복문을 돌리며 해당 알파벳을 ord()를 사용해 아스키 숫자로 바꾼 후,
# # 거기서 97을 뺀 인덱스 위치에 넣는 식으로 리스트에 넣어주겠다.
# # (예: 'a'== 97이므로 97-97=0이니 arr[0]에 a가 word에서 첫번째로 나온 인덱스를 넣는다.)
# word = input()
# for i in range(len(word)):
#     # 만약 이미 첫번째 자리가 저장되고, 두번째로 알파벳이 나온 것이라면
#     # continue 처리를 해서 첫번째 자리값만 저장되도록 한다.
#     if arr[ord(word[i]) - 97] >= 0:
#         continue
#     else:
#         arr[ord(word[i]) - 97] = i
#
# for a in arr:
#     print(a, end=' ')

# # 2675 문자열 반복
# T = int(input())
#
# for tc in range(1, T+1):
#     num, word = input().split()
#     num = int(num)
#     P = ''
#     for w in word:
#         P += w * num
#
#     print(P)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     num, word = input().split()
#     num = int(num)
#     P = ''
#     for w in word:
#         print(w * num, end='')
#     print()

# #1157 단어 공부
#
# # 우선, 대문자 A의 아스키코드는 65, 소문자 a의 아스키코드는 97이다.
# # 즉 대문자 아스키코드에 32를 더해주면 소문자가 되는 것이다.
# # 대, 소문자 상관 없이 가장 많이 사용되는 알파벳이므로 알파벳 언급 횟수를 셀 배열은 26개의 공간을 가진 한개의 리스트만 있으면 충분하다.
#
# arr = [0 for _ in range(26)]
# word = input()
#
# # 10809번 알파벳 찾기 문제처럼 word를 반복문을 돌리며 해당하는 인덱스의 값을 +1 해주면 된다.
# # 여기서 중요한 것은, 소문자는 97을 빼줬지만, 대문자의 경우 65를 빼줘야 한다.
# # (예: 소문자 'a'는 arr[ord('a') - 97], 'A'는 arr[ord('A') - 65] 위치에 넣어야 대소문자 상관 없이 arr[0]의 횟수가 올라간다.
#
# for w in word:
#     # 97 <= ord(w) <= 122 이면 소문자
#     # 65 <= ord(w) <= 90 이면 대문자
#     if 97 <= ord(w) and ord(w) <= 122:
#         arr[ord(w) - 97] += 1
#     elif 65 <= ord(w) and ord(w) <= 90:
#         arr[ord(w) - 65] += 1
#
# # 이제 arr에 들어간 횟수 중 가장 많은 횟수를 가진 알파벳을 구하자.
# # 만약 가장 큰 값이 2개라면 '?'을 출력해줘야 한다.
# # 그래서 만약 최대값과 같은 값이 나오면 cnt를 1 더해주도록 하고,
# # 만약 현재의 최대값보다 큰 값을 만나면 cnt를 1로 초기화해주도록 했다.
#
# max_num = 0
# max_idx = 0
# cnt = 0
# for n in range(len(arr)):
#     if arr[n] > max_num:
#         max_num = arr[n]
#         max_idx = n
#         cnt = 1
#     elif arr[n] == max_num:
#         cnt += 1
#
# # 배열을 다 돈 후, cnt가 1보다 크다면, 즉 최댓값이 여러개라면 ?을 출력한다.
# # cnt가 1보다 작거나 같다면(어차피 1보다 작을 수는 없다.) 해당 인덱스에 65을 더해서 대문자로 출력한다.
#
# if cnt > 1:
#     print('?')
# else:
#     print(chr(max_idx + 65))


# # 1152 단어의 개수
# word = list(input().split())
# print(len(word))


# # 2908 상수
# # 두 수를 입력받으면 거꾸로 읽은 후 크기가 큰 쪽을 답하는 상수의 대답을 출력해보자!
# # 파이썬 내장함수를 사용해서 문자열로 바꿔서 풀 수 있지만, 이번엔 10으로 나눠줘서 자리수를 구하고, 구한 자리수에 다시 10을 곱해 바꿔보려 한다.
#
# def reverse(n):
#     reversed_num = 0
#     for i in range(2, -1, -1):
#         reversed_num += (n % 10) * (10 ** i)
#         n = n // 10
#
#     return reversed_num
#
# A, B = map(int, input().split())
# A = reverse(A)
# B = reverse(B)
#
# if A >= B:
#     print(A)
# else:
#     print(B)


# 5622 다이얼
# 문자를 다이얼에 해당하는 숫자로 변경하고, 숫자+1(1을 입력할 때 2초이므로)를 더해주면 되는 문제.
# 어렵게 풀면 너무 힘들 것 같아서 가장 쉬운 방법으로 풀어보았다.

word = input()
sum = 0

for w in word:
    if w in ['A', 'B', 'C']:
        sum += 3
    elif w in ['D', 'E', 'F']:
        sum += 4
    elif w in ['G', 'H', 'I']:
        sum += 5
    elif w in ['J', 'K', 'L']:
        sum += 6
    elif w in ['M', 'N', 'O']:
        sum += 7
    elif w in ['P', 'Q', 'R', 'S']:
        sum += 8
    elif w in ['T', 'U', 'V']:
        sum += 9
    elif w in ['W', 'X', 'Y', 'Z']:
        sum += 10

print(sum)