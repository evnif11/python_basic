import sqlite3
import datetime

now = datetime.datetime.now()
print(now)

nowdatetime = now.strftime("%Y-%m-%d, %H:%M:%S")
print(nowdatetime)

# DB 생성 및 경로 설정, isolation_level=None 은 오토커밋 옵션
conn = sqlite3.connect(
    '/Users/chanjoo/Documents/Python_Basic/resource/database.db',
    isolation_level=None
    )

# 커서 : 커서가 어딨느냐에 따라 읽어올 데이터가 있는지 없는지 확인 가능해져
c = conn.cursor()

# 테이블 생성
c.execute('CREATE TABLE IF NOT EXISTS \
           users(id INTEGER PRIMARY KEY, username text,\
           email text, phone text, website text, regdate text)')
# 물음표는 튜플 형태로 값 매칭이 됨
c.execute('INSERT INTO users VALUES(1, "kim", "kim@test.com",\
          "010-2423-2323", "kim.com", ?)', (nowdatetime,))
# 한 번에 삽입하기(튜플, 리스트)
userList = (
    (2, 'lee', 'lee@test.com', '010-3232-2342', 'lee.com', nowdatetime),
    (3, 'park', 'park@test.com', '010-3232-2342', 'park.com', nowdatetime),
    (4, 'son', 'son@test.com', '010-3232-2342', 'son.com', nowdatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
               VALUES(?, ?, ?, ?, ?, ?)", userList)
# 데이터 삭제
# conn.execute("DELETE FROM USERS")

# 롤백
# conn.rollback()

# 접속해제
# conn.close()
