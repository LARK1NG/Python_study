# MULTILINE, M
import re
p = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))