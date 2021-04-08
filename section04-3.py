# 파이썬 데이터 타입(자료형)

# 리스트, 튜플
# 자료구조 형태로 저장하여
# 수정, 삭제 등을 용이하게 생산성 좋도록

# 리스트(순서o, 중복o, 수정o, 삭제o)
a = []
b = list()  # 명시적으로도 사용 가능
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'banana', 'orange']
e = [10, 100, ['pen', 'banana', 'orange']]  # 배열(리스트)안의 배열

# 인덱싱
print(d[3])
print(d[-2])  # banana
print(d[0]+d[1])  # 110
print(e[2][2])  # orange
print(e[-1][-1])  # orange

# 슬라이싱
print(d[0:3])  # list로 반환해서 결과 나옴
print(e[2][1:3])  # ['banana', 'orange']

# 연산
print(c + d)  # 하나의 리스트로 합쳐줌
print(c * 3)  # 리스트를 복제해줌
print(str(c[0]) + 'hi')  # 문자열로 형변환해서 같이 출력도 가능

# 리스트 수정, 삭제
c[0] = 77
print(c)  # 리스트 값이 수정되었음

c[1:2] = [100, 1000, 10000]
print(c)  # 값을 삽입

c[1] = ['a', 'b', 'c']
print(c)  # 리스트 자체를 추가도 가능

del c[-1]
print(c)  # 값 삭제

# 리스트 함수 : 조작 제어 기능
y = [5, 2, 3, 1, 4]
print(y)

y.append(6)
print(y)  # 끝에 값 추가

y.sort()
print(y)  # 정렬

y.reverse()
print(y)  # 반대로 정렬

y.insert(2, 7)
print(y)  # 2번 인덱스에 7을 추가할 거야

y.remove(2)  # del은 인덱스의 값을 지웠고
print(y)  # remove 함수는 데이터 값 '2'를 지워버렸음

y.pop()  # 스택
print(y)
y.pop()
print(y)
y.pop()
print(y)  # 마지막 값을 제거해버림

ex = [88, 77]
y.append(ex)  # append는 리스트 자체를 추가
y.extend(ex)  # extend는 원소로 추가 가능
print(y)


# 삭제 : del, remove, pop(언젠가 에러가 나는 점 * 주의)

# 튜플(순서o, 중복o, 수정x, 삭제x)
# 프로그램에 영향을 주는 중요한 키 값
# 변경되면 프로그램 실행에 중요한 영향을 끼치는 것들을 방지하기 위함
# 따라서 메소드 별로 없음

a = ()
b = (1,)  # 값을 넣을 때는 마지막 콤마로 끝내주면 됨
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2], c[3])
print(d[2][-2])
print(d[2:])  # 슬라이싱도 가능
print(d[2][0:2])

print(c + d)  # 연산 가능
print(c * 3)

# 튜플 함수
z = (5, 2, 1, 3, 4, 1, 1)
print(z)
print(3 in z)
print(z.index(5))  # 찾고자 하는 값의 인덱스를 반환해줌
print(z.count(1))  # 1이 몇개야
