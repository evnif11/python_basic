# CSV, 엑셀 쓰고 읽기

# CSV : MIME - text/csv
import pandas
import csv

# 예제 1 : utf-8 혹은 euc-kr 디코딩 방식 염두하기
with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    # next(reader)  # header 제거
    print(reader)
    print(dir(reader))
    print(type(reader))

    for c in reader:
        print(c)

# 예제 2 탭이나 | 로 데이터 구분 되어져 있을 때
with open('./resource/sample2.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f, delimiter='|')
    # next(reader)  # header 제거
    print(reader)
    print(dir(reader))
    print(type(reader))

    for c in reader:
        print(c)

# 예제 3 딕셔너리 변환 (굉장히 유용)
with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)

# 예제 4 개행 없에는 newline 옵션
w = [[1, 2, 3], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    # 흐름을 줘야할 때 if문으로 줄 수 있는 메소드 : writerow()
    for v in w:
        wt.writerow(v)

# 예제 5 한 번에 작성

with open('./resource/sample5.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)


# XSL , XLSX
# openpyxl, xlrd, xlsxwriter, xlwt, xlutils
# pandas를 주로 사용함 (openpyxl, xlrd)
# pip install pandas openpyxl xlrd 컴마 안돼!

# sheetname='', header='3', skiprow='1' 옵션 있음
xlsx = pandas.read_excel('./resource/sample.xlsx')
print(xlsx.head())
print(xlsx.tail())
# 행 열 갯수
print(xlsx.shape)


# 엑셀, csv 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
