# 파이썬 자료구조 (딕셔너리, 집합 셋)
# 웹에서 표준으로 소켓통신 등 데이터
# 표준 구조인 json하고 유사하다

# 딕셔너리(dictionary) : 파이썬의 꽃
# 순서x 중복x 수정o 삭제o

# key와 value로 이루어진 형식
# xml, css, 브라우저 송수신에 활용하는 json -> MongoDB

# 선언 : 열쇠(key)를 가지고 값(value)을 조회한다
# 키는 숫자로 잘 안해, 조회하고자 하는 의미있는 단어로 구성
a = {'name': 'kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello coding'}
c = {'arr': [1, 2, 3, 4, 5]}  # 유연하게 사용 가능

# print(type(a))

# 출력
print(a['name'])  # 직접 접근 (키 에러가 날 수 있음)
print(a.get('name'))  # get으로 안전하게 조회하기
print(a.get('address'))  # 없을 땐 None
print(c.get('arr')[1:3])  # 리스트는 슬라이싱 가능

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)

a['rank'] = [1, 3, 5]
a['rank2'] = (1, 2, 3,)
print(a)

# keys, values, items 각각 용어
print(a.keys())  # 생긴건 리스트처럼 생겼는데 인덱스 접근 불가?
print(list(a.keys()))  # 리스트로 형변환해야 접근 가능

temp = list(a.keys())
print(temp[1:4])

print(a.values())  # 반복문을 사용하게 되면 대량의 데이터 너무 편해져
print(a.items())
print(list(a.items()))  # list안의 튜플로 조회됨

print(2 in b)  # key가 2 인게 있니
print('name' in a)  # key가 name 인게 있니
print('name' not in b)

# 집합(Sets) : 과학 연산 머신러닝 공식 내부적 오픈소스 케라스에 많이 쓰임
# 순서x 중복x

a = set()
b = set([1, 2, 3, 4])
c = set([1, 5, 6, 6])

print(type(a))
print(c)  # 중복을 허용하지 않는다

# 튜플 리스트로 변환해서 슬라이싱 가능
# 셋은 주로 변환해서 사용함
t = tuple(b)
print(t)  # 괄호가 소괄호로 바뀜 (1,2,3,4)

l_sets = list(b)
print(l_sets)  # reverse, sort 다 사용가능해짐

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)  # 교집합

print(s1.union(s2))
print(s1 | s2)  # 합집합

print(s1.difference(s2))
print(s1 - s2)  # 차집합

# 추가 제거 가능함
s3 = set([7, 8, 10, 15])
s3.add(18)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))
