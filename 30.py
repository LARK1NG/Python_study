a = {1: '파랑구름', 2: '이현준', 3: '민MIN준JUN'}

print(a.keys())

print(a.values())

print(a.items())

for k in a.keys():
    print(k)

for v in a.values():
    print(v)

for k, v in a.items():
    print("키는: " + str(k))
    print("벨류는: " + v)