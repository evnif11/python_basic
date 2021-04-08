# 파이썬 흐름 제어
# 반복문
#
# 코딩의 핵심은 조건 해결이다
# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1  # 증감을 시켜줘야지 반복하지

for v2 in range(10):
    print("v2 is :", v2)

# 1 ~ 100 합
total = 0
for i in range(11):
    total += i
print("total is :", total)

sum1 = 0
i = 0
while i <= 10:
    sum1 += i
    i += 1
print("1 ~ 10 :", sum1)
print("반복횟수 :", i)

# sum 이라는 함수 사용 가능
print(sum(range(1, 101)))
print(sum(range(1, 11, 5)))


# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트 / 튜플, 집합, 사전 => 모두 반복 가능
# iterable 리턴 함수 : range, reversed, enumerate, filter, map,zip

names = ["Kim", "Park", "Cho", "Choi", "You"]
for name in names:
    print("You are :", name)

word = "Dreams"
for s in word:
    print("Words : ", s)

my_info = {
    "name": "kim",
    "age": 33,
    "city": "seoul"
}

for key in my_info:
    print("1", key)

for key in my_info.keys():
    print("2", key)

for value in my_info.values():
    print("3", value)

for k, v in my_info.items():
    print("4", k, v)


# 문제
name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())


# break : for문에서 사용하는 아주 중요한 조건
# 내가 찾고자 하는 값이 중간에 있을 때,
# 찾고나서도 순회한다. 자원낭비임.
# 조건을 걸어줘서 중단을 시킬 수 있음.

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 39]

for n in numbers:
    if n == 33:
        print("found: 33!")
        break  # 찾고나서 중단시켜줌
    else:
        print("not found: 33")


# for - else 구문 (독특한 문법)
# 반복문이 정상적으로 수행된 경우 블럭 수행됨
# break 만났을 경우엔 수행되지 않음
for n in numbers:
    if n == 33:
        print("found: 33!")
    else:
        print("not found: 33")
else:
    print("...")


# continue : 조건문으로 바로 이동, 하위 조건 수행 X
it = ["1", 2, 5, True, 4.3, complex(4)]

# 리스트 안에 실수형이 있는지 찾고 싶어
for v in it:
    if type(v) is float:
        continue

    print("타입 : ", type(v))

name = "chanjoo lee"
print(list(reversed(name)))
print(tuple(reversed(name)))
