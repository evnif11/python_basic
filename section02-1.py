# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본출력
print('hello python!')
print("hello python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T','E','S','T', sep='')
print('2019','02','19', sep='-')
print('niceman','google.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black paradise', end=' ')
print('piano notes')

# format 사용 [], {}, () 대괄호 중괄호 소괄호
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You','Me'))
print('{a} are {b}'.format(a='You', b='Mine'))

# %s 문자 %d 정수 %f 실수
print("%s's favorite number is %d" %('Chanjoo', 7))

print("Test1: %5d, price: %4.2f" %(778, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(234, 5432.342))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=1323.412))

"""
참고: escape code
\000 널문자
"""

print("'YOU'")
print('\'you\'')
print('\\you\\\n')
print('\t\t\ttest')

n = int(input())

for i in range(n):
    res = " " * (n - i - 1) + "*" * (i+1)
    print(res)
