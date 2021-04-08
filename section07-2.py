# 클래스 상속, 다중상속(파이썬 특징)
# 코드의 생산성 유지보수 가독성

# 자바는 다중상속 지원안하고 인터페이스를 지원함

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


# 상속
class BMWCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)  # 부모 클래스에 넘겨줘야할 변수
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):  # 부모한테도 있는 메소드
        print(super().show())  # 부모것도 호출해
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)


# 일반 사용
model1 = BMWCar('520d', 'sedan', 'red')  # 인스턴스 생성

print(model1.color)  # super
print(model1.type)  # super
print(model1.car_name)  # sub
print(model1.show())  # super
print(model1.show_model())  # sub
print(model1.__dict__)

# Method Overriding(오버라이딩) : 자식에서 기능을 개선 혹은 추가한 것
model2 = BenzCar("220d", 'suv', 'black')
print(model2.show())  # 메소드를 재구현

# Parent Method Call (42줄)
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())

# Inheritance info (상속정보): 상속 관계가 깊을 때 쉽게 표현
print(BMWCar.mro())  # BMWCar -> Car -> object
print(BenzCar.mro())


# 예제 2 (다중상속) 보통은 두개 정도

class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
print()
print(A.mro())
