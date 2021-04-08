# 문자열, 문자열 연산, 슬라이싱

str1 = "I am a Boy."
str2 = "Niceman"
str3 = ''
str4 = str('')

print(len(str1), len(str2), len(str3))

# 이스케이프 문자 (역슬래시)
escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

# \t 탭키
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw string : 경로 표시할 때 많이 씀
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

raw_s2 = r'\\a\\a'
print(raw_s2)

# 멀티라인 : 역슬래시가 이어진다는 것을 알려줌
# multi = '\'
# print(multi)

# 문자열 연산 : 문자를 곱하거나 더할 수 있다
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'Niceman'
# 문자열은 immutable : 한 번 할당되면 수정 불가능, 순회가능함

print(str_o1 * 100)
print(str_o2 + str_o3)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수 : 파이썬에 문자열 처리에 좋은 함수들이 많다
"""
한 번에 주석처리는 [ command + / ]
"""
# a = 'Nice man'
# b = 'orange'

# print(a.isdecimal())
# print(a.endswith('n')) # check 할 때 유용하게 쓰임
# print(b.capitalize()) # 첫 번째 대문자로 바꿔줌
# print(a.replace('Nice', 'Good')) # 대체 가능
# print(list(reversed(b))) # list 형태로 리버스도 가능함


# 문자열 슬라이싱(가장 중요)
# 문자열은 <인덱싱> 되어있기 때문에
# 자기 공간에 값이 저장 되어있는 immutable 수정 불가능한 변수
# 딕셔너리, 배열안의 배열 등은 조심해서 써야한다

a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])  # 길이를 쉽게 정할 수 있어 편하다
print(a[0:len(a)-1])
print(a[:4])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])  # 처음부터 끝까지 나오는데, 역순으로
