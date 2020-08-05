import re
# .* (loop de maior tamanho possivel do caractere)
# .+ (no minimo 1 ocorrencia do caractere)
# .? (Uma ou 0 ocorrencias de um caractere)

print(re.search(r"py.*n","pygmalion")) # vai procurar palavras que começam com py e tem qualquer caractere (incluindo 0 caracteres), repetido quantas vezes for possivel no meio e terminado em n
# <re.Match object; span=(0, 9), match='pygmalion'>

print(re.search(r"py.*n","python programing")) # vai pegar quantos caracteres for possivel
# <re.Match object; span=(0, 16), match='python programin'>

print(re.search(r"py[a-z]*n","pyhon programing")) # espaco nao esta entre [a-z]
# <re.Match object; span=(0, 5), match='pyhon'>

print(re.search(r"o+l+","goldfish")) # o+l+ vai procurar no minimo uma , ou mais ocorrencias em sequencia de o seguido de l
# <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+","woolle"))
# <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+","boil")) # nao possui no minimo 1 combinacao de O seguido de L
# None

def repete_letra (text): # vai verificar se tem ao menos 2 A's(upper ou lower case) com qualquer combinacao de caracteres no meio
    resultado = re.search(r"[Aa].*[Aa]+",text)
    return resultado != None

print(repete_letra("banana")) # True
print(repete_letra("pineapple")) # False
print(repete_letra("Animal Kingdom")) # True
print(repete_letra("A is for apple")) # True

print(re.search(r"S?earch","earch"))
# <re.Match object; span=(0, 5), match='earch'>
print(re.search(r"S?earch","Search and destroy"))
# <re.Match object; span=(0, 6), match='Search'>