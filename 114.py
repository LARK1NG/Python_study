f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()