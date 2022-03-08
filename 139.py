# 메타문자 |
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)