import re

expression = r"a[bcd]*b"
result = re.search(expression,"abcbd")
print(result)
# <re.Match object; span=(0, 4), match='abcb'>

print(re.search(r"<.*?>","<html><head><title>Title</title>")) # *? nao e greedy ,logo da match no primeiro >
# <re.Match object; span=(0, 6), match='<html>'>