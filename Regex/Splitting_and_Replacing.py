import re

# split - vai ultilizar qualquer regex como separador
# sub - subistitui o match pela string desejada
# \2 - vai representar o gupo 2 nesse caso

print(re.split(r"[.?!]","One sentence. Another one? And last one!")) # caracteres dentro do colchetes nao precisam de \
# ['One sentence', ' Another one', ' And last one', '']
print(re.split(r"([.?!])","One sentence. Another one? And last one!")) # Agrupar para adicionar os caracteres a lista
# ['One sentence', '.', ' Another one', '?', ' And last one', '!', '']

print(re.sub(r"[\w.%-+]+@[\w.+-]+","[REDACTED]","Recived an email for Myemail99@email.com"))
# Recived an email for [REDACTED]

print(re.sub(r"^([\w .-]*), ([\w .-]*)$",r"\2 \1","Lovelace, Ada")) # \2 e \1 representam os grupos 2 e 1 respectivamente
# Ada Lovelace