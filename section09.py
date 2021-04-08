# 파일 읽기 쓰기
# 읽기 모드 : r
# 쓰기 모드 : w (기존 파일 삭제)
# 추가 모드 : a
# .. : 상대경로 , . : 절대 경로

# 예제 1 : 파일 읽기

f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()
print("-------------------------------------------")
print("-------------------------------------------")
# 예제 2 : with 는 클로즈 생략 가능
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print("-------------------------------------------")
    print(iter(c))

print("-------------------------------------------")
print("-------------------------------------------")

# 예제 3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print("-------------------------------------------")
print("-------------------------------------------")

# 예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>', content)
    content = f.read()  # 내용 없음
    print('>', content)


print("-------------------------------------------")
print("-------------------------------------------")

# 예제 5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='*** ')
        line = f.readline()

# 예제 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' *** ')

print()

print("-------------------------------------------")
print("-------------------------------------------")

# 예제 7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

# 평균 구하기
print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기
# 예
with open('./resource/text1.txt', 'w') as f:
    f.write("niceman\n")

with open('./resource/text1.txt', 'a') as f:
    f.write("goodman\n")

# 예제 3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(0, 6):
        f.write(str(randint(0, 100)))
        f.write('\n')

with open('./resource/text3.txt', 'w') as f:
    list = ['kim\n', 'lee\n', 'jay\n']
    f.writelines(list)

with open('./resource/text4.txt', 'w') as f:
    print('log 기록 test', file=f)
