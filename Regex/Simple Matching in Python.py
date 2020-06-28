import re

resultado = re.search(r"aza","plaza") # r representa raw string
print(resultado)
#<re.Match object; span=(2, 5), match='aza'>
resultado = re.search(r"aza","bazzar") 
print(resultado)
#None
def verifica_vogal(texto):
    resultado = re.search(r"a.e.i",texto)
    return "Sequencia não encontrada" if resultado == None else "sequencia encontrada"

print(verifica_vogal("academia"))
# True
print(verifica_vogal("aerial"))
# False
print(verifica_vogal("paramedic"))
# True