# 예외란 결국 에러를 뜻한다.
# 무결성한 코딩은 존재하지 않는다.
# 예외 처리를 하면서 더 견고한 코딩을 해나가는 것이 중요

# 문법적으론 에러는 린터로 잡으면 되지만,
# 런타임 에러는 실행시에 나타나는 것

# 1. Systax Error (문법 오류)
# 2. Name Error (참조 변수가 없을 때) : a,b print(c)
# 3. Zero Division Error (0으로 나눴을 때 에러) : print(10/0)
# 4. Index Error (인덱스 범위를 오버) a = [0, 1, 2] print(a[7])
# 5. Key Error(딕셔너리 타입에서 없는 키 값 반환할 때) : dic['name'] 추천>> dic.get('name')
# 6. Attribute Error(모듈, 클래스에 없는 속성이나 메소드 사용시에 발생) : time.month()
# 7. Value Error(참조 값이 없을 때) : a = [0, 1, 2] a.remove(10) a.index(5)
# 8. File Not Found Error(파일이 경로에 없을 때) : with open('text.txt', 'r')
# 9. Type Error(타입이 다른 경우에) : a = [] b = () 이럴 땐 형변환(캐스팅)해줘야함 list(b)

# try: 에러가 발생할 가능성 있는 코드 실행
# except: 에러명 1
# except: 에러명 2
# else: 정상 실행됐을 경우에
# finally: 항상 실행

name = ['kim', 'lee', 'park']

try:
    x = 'kim'
    y = name.index(x)
    print('{} found it in name.' .format(x))
except ValueError:
    print('Not found.. Value Error occured')
except IndexError:
    print('Not found.. Error occured')
except Exception:
    print('Error')
else:
    print('ok else')  # 정상 실행
finally:
    print('whatever')


# raise 직접 에러 발생
