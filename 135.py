# DOTALL S
import re
# p = re.compile('a.b')
# m = p.match('a\nb')
# print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)