# --url--
# https://www.acmicpc.net/problem/2475

# --title--
# 2475번: 검증수

# --problem_description--
# 컴퓨터를 제조하는 회사인 KOI 전자에서는 제조하는 컴퓨터마다 6자리의 고유번호를 매긴다. 고유번호의 처음 5자리에는 00000부터 99999까지의 수 중 하나가 주어지며 6번째 자리에는 검증수가 들어간다. 검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.

# 예를 들어 고유번호의 처음 5자리의 숫자들이 04256이면, 각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81 을 10으로 나눈 나머지인 1이 검증수이다.

# --problem_input--
# 첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.

# --problem_output--
# 첫째 줄에 검증수를 출력한다.

 
import sys

# 1
# a, b, c, d, e = map(int, sys.stdin.readline().split())

# num = a**2 + b**2 + c**2 + d**2 + e**2

# res = num % 10

# print(res)

# 2
# input = sys.stdin.readline

# s = [i**2 for i in map(int, input().split())]

# print(sum(s) % 10)

# 3
nums = list(map(int, input().split()))

res = 0

for i in nums:
    res += i**2

print(res%10)