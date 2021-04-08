# 데이터 타입
import math


v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "Kim",
    "age": 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {3, 5, 7}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))
print(type(v_dict))

i1 = 39
i2 = 939
big_int1 = 999999999999999
big_int2 = 777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)  # 지수
print(f3 + i2)


result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10
print(type(a), type(b))

result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

# 연산자
print(10/3)  # 나눗셈
print(10//3)  # 몫
print(10 % 3)  # 나머지

# 단항연산자
y = 100
y += 100
print(y)

# 수치 연산 함수
print(abs(-7))  # 절댓값
n, m = divmod(100, 8)  # 100을 8로 나눈 몫과 나머지가 각각
print(n, m)


print(math.ceil(5.1))  # 5.1보다 큰 가장 작은 정수는 6
print(math.floor(3.874))  # 3.874보다 작은 가장 큰 정수 3
