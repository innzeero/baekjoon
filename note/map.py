# map은 리스트의 요소를 지정된 함수로 처리해주는 함수이다
# map은 원본리스트를 변경하지 않고 새 리스트를 생성한다

# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

# 만약 실수가 저장된 리스트가 있을 때 이 리스트의 모든 요소를
# 정수로 변환하려면 어떻게 해야 할까?
# for문으로 돌리는 방법을 생각해 볼 수 있다
a = [1.7, 2.3, 3.8, 4.9]
# for i in range(len(a)):
#     a[i] = int(a[i])

# print(a) # [1, 2, 3, 4]

# for문이 도는 범위를 range(len(a))를 줌으로써
# 리스트 a의 각 인덱스를 가져온다
# 그리고 가져온 인덱스로 요소 하나 하나에 차례로 접근하여 int로 변환한 뒤 다시 저장한다
# 모든 요소를 하나씩 변환하는 방식이니 번거로운 듯 하다
# 이 때 map을 사용하면 편리하다

a = list(map(int, a))
print(a) # [1, 2, 3, 4]

# 2줄을 사용한 for문에 비해 map을 사용하니 코드가 1줄로 줄어들었다
# map에 int와 리스트를 넣으면 리스트의 모든 요소를 int를 사용해서 변환한다
# 그 다음에 list를 사용해서 map의 결과를 다시 리스트로 만들어준다

# 사실 map에는 리스트뿐만 아니라 모든 반복 가능한 객체를 넣을 수 있다

# -----------------------------------------------------------------------------------------
# -> 반복 가능한 객체란?
# 반복 가능한 객체는 말 그대로 반복할 수 있는 객체인데 
# 우리가 흔히 사용하는 문자열, 리스트, 딕셔너리, 세트가 반복 가능한 객체이다
# 즉, 요소가 여러 개 들어있고, 한 번에 하나씩 꺼낼 수 있는 객체이다
# 객체가 반복 가능한 객체인지 알아보는 방법은 객체에 __iter__ 메서드가 들어있는지 확인해보면 된다
# dir 함수를 사용하면 객체의 메서드를 확인할 수 있다

print(dir([1,2,3]))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', 
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 
# 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# -----------------------------------------------------------------------------------------

# range를 사용해서 숫자를 만든 뒤 숫자를 문자열로 변환해보자
a = list(map(str, range(10)))
print(a) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 리스트 요소들이 '' 로 묶여있다 == 문자열


