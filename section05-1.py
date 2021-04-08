# 파이썬 흐름제어 (제어문)
# 조건문

print(type(True))
print(type(False))


if True:
    print("Yes")

if False:
    print("No") # 아예 출력되지 않는다 참 일때만 실행되니까
else:
    print("Yes2")

# 관계연산자

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

# <종류>
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

city = ""
if city:
    print("True")
else:
    print("False")

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and:', a > b and b > c)  # 둘 다 맞아야 True(1)
print('or:', a > b or c > b)  # 둘 중 하나만 맞아도 True(1)
print('not:', not a > b)  # 반대임

# 우선순위 : 산술 > 관계 > 논리 순서
print('ex: ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("{}님은 합격입니다".format("찬주"))
    print("%s님 축하합니다" % ("찬주"))
else:
    print("죄송합니다")


# 다중조건문
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("F")


# 중첩조건문

age = 19
height = 183

if age >= 20:
    if height >= 170:
        print("%s님은 지원 가능합니다" % ("건우"))
    elif height >= 160:
        print("지원 가능")
else:
    print("20세 미만은 지원 불가능합니다.")
