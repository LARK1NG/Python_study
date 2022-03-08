# 전방탐색: 부정형 (?!)
import re
p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
tutoexec.jpg
""")
print(l)