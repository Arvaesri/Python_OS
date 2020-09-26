import re

pattern = r"(\b[INFO|ERROR][\w ']*\b) [\[\]#\d ]*\(([\w \.]*)\)"
line = "Jan 31 08:22:37 ubuntu.local ticky: INFO Created ticket [#2860] (mcintosh)"
find = re.search(pattern,line)
print(find.groups())
print(find.group())
print(find.group(1))
print(find.group(2))