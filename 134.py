import re
p = re.compile('[a-z]+')
m = p.match('life is too short')
print(m.group())
print(m.start())
print(m.end())
print(m.span())