# 타이핑 게임

import time
import random
# 소리 삽입 , 데이터베이스 연동
import datetime
import pygame
import sqlite3

pygame.init()

# DB 생성
conn = sqlite3.connect("./resource/gameDatabase.db", isolation_level=None)
# 커서 생성
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, \
           correct_count INTEGER, record text, regtime text)")


words = []

n = 1  # 게임 시도 횟수
cor_cnt = 0  # 맞춘 갯수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words)

input("Ready? Press Enter key!")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print('Question . {}'.format(n))
    print(q)

    x = input()

    print()

    if str(q).strip() == str(x).strip():
        mysound = pygame.mixer.Sound('./sound/good.wav')
        mysound.play()
        print("Pass!")
        cor_cnt += 1
    else:
        mysound = pygame.mixer.Sound('./sound/bad.wav')
        mysound.play()
        print("wrong")

    n += 1

end = time.time()

et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("분발하세요")
print()
print("게임 시간 : ", et, "초", "정답 갯수 : {} / 5".format(cor_cnt))

# 기록 DB 삽입
cursor.execute("INSERT INTO records('correct_count', 'record', 'regtime') VALUES(?, ?, ?)", (cor_cnt, et, datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%s")))


# 시작 지점
if __name__ == "__main__":
    pass
