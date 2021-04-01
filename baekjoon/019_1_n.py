# --url--
# https://www.acmicpc.net/problem/8393

# --title--
# 8393번: 합

# --problem_description--
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# --problem_input--
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# --problem_output--
# 1부터 n까지 합을 출력한다.

n = int(input())
res = 0

for i in range(1, n+1):
    res += i
print(res)

