import re

resultado = re.search(r"[a-z]way","End of the highway") #Qualquer letra de [a-z]
print(resultado)
#<re.Match object; span=(14, 18), match='hway'>

def check_pontuacao(texto):
    resultado = re.search(r"[':;.?!]",texto)
    return resultado != None

print(check_pontuacao("Uma sentenca que termina com."))
# True
print(check_pontuacao("Uma frase sem ponto"))
# False
print(check_pontuacao("Aren't regular expressions awesome?"))
# True

# Match em todos caracteres exeto os da lista-[^]
resultado = re.search(r"[^a-zA-Z]","This is a sentence with Space...")
print(resultado)
# <re.Match object; span=(4, 5), match=' '>
resultado = re.search(r"[^a-zA-Z ]","This is a sentence without Space.")
print(resultado)
# <re.Match object; span=(32, 33), match='.'>

# Match em uma expressao ou outra - |
resultado = re.search(r"cat|dog","I like cats")
print(resultado)
# <re.Match object; span=(7, 10), match='cat'>

resultado = re.search(r"cat|dog","I like both dogs and cats") # retorna a primeira opcao encontrada
print(resultado)
# dog

# Encontrando todas as possiveis matchs
resultado = re.findall(r"cat|dog","I like both dogs and cats")
print(resultado)
# ['dog', 'cat']