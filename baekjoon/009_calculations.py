# --url--
# https://www.acmicpc.net/problem/10869

# --title--
# 10869번: 사칙연산

# --problem_description--
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

# --problem_input--
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

# --problem_output--
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)  # 나눗셈 결과 중 몫만 구하는 방법 : //
print(a % b)  # 나눗셈 결과 중 나머지만 구하는 방법 : %
