# --url--
# https://www.acmicpc.net/problem/1000

# --title--
# 1000번: A+B

# --problem_description--
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# --problem_input--
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# --problem_output--
# 첫째 줄에 A+B를 출력한다.

# 1)
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)

# 2)
a, b = input().split()
print(int(a) + int(b))

# 3)
a, b = map(int, input().split())  # 공백을 기준으로 숫자를 입력받아 각각 a, b라는 변수에 저장
print(a + b)  # a, b를 더한 값을 출력


# python에서 문자를 입력받기 위해서는 input()을 사용한다
# 2개 이상의 문자를 입력받아야 할 때에는 split()을 사용하는데, ()안에
# 입력 받을 숫자를 구분할 기호를 입력한다
# 현재는 공백을 기준으로 두 숫자가 구분 되기 때문에 위와 같이 작성하였다
# if, 콤마로 구분된다면 split(,)와 같이 작성하면 된다
# input()은 기본적으로 문자열을 입력 받는 것이기 때문에
# 1)처럼 입력 받은 후 각 숫자를 정수형으로 바꿔주는 int()를 사용해도 되고
# 2)처럼 출력을 할 때 바로 int()를 써줘도 된다
# 하나하나 int형으로 바꾸지 않아도 되는 방법은?
# 3)처럼 map을 사용하면 여러 개의 입력 된 문자를 받아 바로 정수형으로 받을 수 있다!
