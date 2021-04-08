# 모듈(각각의 파일), 패키지(폴더 디렉토리로 관리, 코드를 논리적으로 묶어)
# 모듈 사용 및 Alias 설정
# 패키지 사용의 장점
# 파이썬의 강력한 원칙 : 모두 패키지 형태로 제공함, 배포

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))  # 리스트 형태로 반환
print("ex1 : ", Fibonacci().title)  # 클래스 생성후 타이틀 메소드 출력

# 사용2 (메모리 많이 차지해서 권장 안함)
# from pkg.fibonacci import * # 전부 가져온다

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)  # 클래스 생성후 타이틀 메소드 출력


# 사용3 엘리야스
from pkg.fibonacci import Fibonacci as fb

print("ex3 : ", fb.fib2(100))
print("ex3 : ", fb().title)


# 사용4
import pkg.calculations as c
print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5 (권장, 리소스 낭비를 줄여라)
from pkg.calculations import div

print("ex5 : ", int(div(100,10)))

# 사용 6
import pkg.prints as p
import builtins
p.prt()
p.prt2()
print(dir(builtins))
