import sqlite3

# DB 파일 조회, 없으면 생성됨
conn = sqlite3.connect('/Users/chanjoo/Documents/Python_Basic/resource/database.db')

# 커서 바인딩
c = conn.cursor()

# 조회
# c.execute("SELECT * FROM users")

# 커서 위치 변경
# 1개 로우 선택
# print(c.fetchone())
# # 지정된 로우 선택
# print(c.fetchmany(size=2))
# print(c.fetchall())

# 순회
for c in c.fetchall():
    print(c)

# Where Retrieve1
param = (3, )
c.execute("SELECT * FROM users WHERE id=?", param)
print(c.fetchone())
print(c.fetchall())

# Where Retrieve2
param2 = 2
c.execute("SELECT * FROM users WHERE id='%s'" % param2)
print(c.fetchone())
print(c.fetchall())

# Where Retrieve3
c.execute("SELECT * FROM users WHERE id=:Id", {"Id": 4})
print(c.fetchone())
print(c.fetchall())

# Where Retrieve4
c.execute("SELECT * FROM users WHERE id IN(%d, %d)" % (1, 3))
print(c.fetchone())
print(c.fetchall())

# Where Retrieve5
param3 = (1, 2)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param3)
print(c.fetchall())

# Where Retrieve6
c.execute("SELECT * FROM users WHERE id=:Id1 OR id=:Id2", {"Id1": 2, "Id2": 4})
print(c.fetchall())


# Dump
with conn:
    with open('/Users/chanjoo/Documents/Python_Basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print("complete")

conn.close()
