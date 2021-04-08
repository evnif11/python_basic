# section02-2
# 몸풀기 코딩

# import this
import sys

# 파이썬 기본 인코딩, 입출력은 UTF-8
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Goodboy!')

# 변수 선언
myname = 'Goodboy'

# 조건문
if myname == 'Goodboy':
    print('ok')
    # indent(띄어쓰기)도 문법이다

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d =' % (i, j), i*j)


# 함수 선언
def greeting():
    print("안녕하세요, 반갑습니다")  # 선언한 것이라 아무것도 출력안됨


greeting()


# 클래스
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
