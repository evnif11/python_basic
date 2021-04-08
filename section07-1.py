# 클래스의 이해
# self, class, instance 변수

# 클래스, 인스턴스의 차이 : 변수를 할당, 인스턴스화
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간, 각자 네임스페이스 가짐
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수

# 예제1
# 클래스 이름은 대문자로, 띄어쓰기 첫글자도 대문자로

# 속성(성별,이름)
# 메소드(걷다,뛰다,움직이다)로 구성된다
class UserInfor:
    # 속성
    def __init__(self, name):  # 초기화
        self.name = name

    # 메소드
    def user_info_p(self):
        print("name :", self.name)


# 네임스페이스
user1 = UserInfor("Kim")
user1.user_info_p()
print(user1.name)

user2 = UserInfor("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)


# 예제2
# self의 이해
class SelfTest:
    def function1(self):  # 클래스의 메소드(매개변수 없음)
        print('func1 called')

    def function2(self):  # 인스턴스 메소드
        print('func2 called')


self_test = SelfTest()
self_test.function2()
SelfTest.function2(self_test)

# self를 통해서 어떤 함수인지 식별 가능해짐


# 예제3
# 클래스 변수 , 인스턴스 변수
class WareHouse:
    # 클래스 변수 : 하나의 변수로 모든 인스턴스들이 공유함
    stock_num = 0  # self가 없기 때문

    def __init__(self, name):  # 초기화
        self.name = name
        WareHouse.stock_num += 1  # 창고가 생길 때마다

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('kim')
user2 = WareHouse('Park')
user3 = WareHouse('lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)  # 'stock_num': 3 클래스 변수는 모두가 공유하기 때문에

print(user2.name)

del user2
print(user1.stock_num)  # 자기 네임스페이스에 없으면 클래스 네임 스페이스 가서 변수 찾음
