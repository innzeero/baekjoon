
# --url--
# https://www.acmicpc.net/problem/15596

# --title--
# 15596번: 정수 N개의 합

# --problem_description--
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

# 작성해야 하는 함수는 다음과 같다.

# --problem_input--

def solve(a):
    ans = sum(a)
    return ans

a = [1, 2, 3, 4]
# print(solve(a))

def solve_2(a):
    ans = 0
    for i in a:
        ans += i
    return ans

print(solve_2(a))
        
