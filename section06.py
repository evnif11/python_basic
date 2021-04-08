# 함수 정의 및 람다 사용

# 반복적인 행위를 함수를 작성해 사용한다.
# 함수 하나에 한 가지 기능만


# 함수 정의
# def 함수명(parameter):
#       code

# 함수 호출
# 함수명()
# 함수명(parameter)

# 함수 선언 위치가 중요하다


# 예제1
def send_sms(x):
    print("hello", x)


send_sms("chanjoo")
send_sms(777)


# 예제2 리턴이 있는 함수
# 프린트와 리턴의 차이

def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y


c = f1(10)
print(c)

# 예제3 다중리턴
# 리턴은 보통 하나로 하는 언어들이 많음


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3, type(val3))


# 데이터 타입 반환
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul2(100)
print(lt, type(lt))

# 예제4 다양한 매개변수를 받아서 쓸 수 있음
# *args, *kwargs => 별표 하나는 튜플로
# enumerate : 인덱스해줌


def args_func(*args):  # 가변
    for i, v in enumerate(args, 1):
        print(i, v)


args_func('kim', 'lee', 'park')  # 튜플 형태


# kwargs : 100개든 1000개든 가변적으로 넘길 수 있음
# 별표 두개는 딕셔너리 타입으로
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1="kim", name2="park", name3="lee")


# 전체 혼합
# 앞에 두개는 필수적으로 입력해야하는 인자들임
# 뒤에 두개는 가변적으로 활용가능 (써도되고 안써도 되고)
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 30)
example_mul(10, 30, 'park', 'kim', age1=24, age2=36)


# 중첩함수(클로저) : 변수의 선언을 줄일 수 있고, 메모리관리를 효율적으로 할 수 있음
# 데코레이터 : 함수를 입력변수로 받는다. 기존 함수의 변경 없이 추가적 기능을 덧붙일 수 있도록 하는 함수

# 클로저
# 변수의 스코프?

a = 1


def nested_func(num):
    a = 2

    def func_in_func(num):    # 1. 처음엔 실행이 안되고
        print('>>>', num)     # 4. 최종 출력

    i = 0
    funcs = []
    while i < 3:
        b = i * 2

        def func():
            print(b)
        funcs.append(func)
        i += 1
    funcs[-1]()

    print('in func')          # 2. 실행된 후에
    func_in_func(num + 10000) # 3. 내부 함수 호출하면
    print(a)


nested_func(10000)


# 예제6 힌트(hint)
# 명시적으로 입출력값의 타입을 알려줄 수 있다

def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul2(5))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(heap 초기화) -> 메모리 초기화


# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))
print(var_func(10))

# 람다식 (데이터 전처리, 웹에서 사용할 게시판 데이터 가져와서 내용수정, 형태소 분석)
lambda_mul_10 = lambda num: num * 10
print(">>>", lambda_mul_10(19))


# 함수를 매개변수로 넘길 때 편하다, 메모리 절약
def func_final(x, y, func):
    print(x * y * func(10))


func_final(10, 10, lambda_mul_10)
func_final(10, 10, lambda x: x * 100)
