import re

# Obter uma lista de nomes separados por virgula
resultado = re.search(r"^(\w*), (\w*)$","Lovelace, Ada")
print(resultado)
# <re.Match object; span=(0, 13), match='lovelace, ada'>

print(resultado.groups()) # O numero de grupos vai depender os grupos que foram separados acima , no caso 2
# ('Lovelace', 'Ada')
print(resultado[0]) # O index 0 vai retornar a string inteira
# Lovelace, Ada
print(resultado[1]) # O index posterior a 0 vai retornar o grupo respectivo ao index
# Lovelace
print(resultado[2])
# Ada

def flip_name(nome):
    resultado = re.search(r"^([\w \.-]*), ([\w \.-]*)$",nome)
    if resultado == None:
        return nome
    return "{} {}".format(resultado[2], resultado[1])

print(flip_name("Hopper, Grace M."))
# Grace M. Hopper