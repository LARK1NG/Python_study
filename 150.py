# 문자열 바꾸기 sub
import re
p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes'))