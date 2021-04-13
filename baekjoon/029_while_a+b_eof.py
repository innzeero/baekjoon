# --url--
# https://www.acmicpc.net/problem/10951

# --title--
# 10951번: A+B - 4

# --problem_description--
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# --problem_input--
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# --problem_output--
# 각 테스트 케이스마다 A+B를 출력한다.

# 1. 에러 예외처리
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except EOFError:
#         break

# EOFError? 
# End Of File, 파일의 끝을 의미
# 입력 도중에 파일의 끝을 만나면 EOFError가 발생한다
# 위 문제는 입력이 끝날때까지 임의의 개수의 수를 입력받아야 한다


# 2. sys 사용
import sys

lines = sys.stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    print(a+b)

# sys.stdin.readlines() 은 파일의 끝 부분까지 한 번에 가져올 수 있다
# 가져온 내용 안에서 반복문을 사용



