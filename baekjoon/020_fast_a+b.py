# --url--
# https://www.acmicpc.net/problem/15552

# --title--
# 15552번: 빠른 A+B

# --problem_description--
# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

# None

# None

# None

# 또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

# None

# None

# --problem_input--
# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

# --problem_output--
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

import sys

t = int(sys.stdin.readline())

# int()로 감싸지 않을 경우의 출력 형태
# print(t)
# print(type(t))
# 2
# 2

# <class 'str'>
# sys.stdin.readline()은 한 줄 단위로 입력 받기 때문에, 개행문자가 같이 입력받아진다
# 만약 5를 입력한다면 5\n 이 저장되기 때문에 개행문자를 제거해야 한다
# 또한, 변수 타입이 문자열 형태로 저장되기 때문에 정수로 사용하기 위해서는 형변환이 필요하다

# a, b = map(int, sys.stdin.readline().split())
# map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수
# 위와 같이 사용하면 a, b에 대해 각각 int 형으로 type 변환이 가능하다
# a, b 입력 받는 것을 t번 만큼 반복해야 하기 때문에 a, b를 받는 위 코드를 for문 안에 넣어야 한다

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    # print(a, b)
    print(a+b)