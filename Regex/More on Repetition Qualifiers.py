import re

# {5} - Qualificador de repeticao numerica , repete a expressao anterior 5 vezes

print(re.search(r"[a-zA-Z]{5}","A ghost")) # Nesse caso vai dar match em palavras de 5 letras
# <re.Match object; span=(2, 7), match='ghost'>
print(re.search(r"[a-zA-Z]{5}","A scary ghost")) # O match vai ser na primeira palavra de 5 letras
# <re.Match object; span=(2, 7), match='scary'>
print(re.findall(r"[a-zA-Z]{5}","A scary ghost apeared")) # Da match em palavras mais longas
# ['scary', 'ghost', 'apear']
print(re.findall(r"\b[a-zA-Z]{5}\b","A scary ghost apeared")) # Ultilando o \b para indicar palavras com exatamente 5 letras
# ['scary', 'ghost']
print(re.findall(r"[a-zA-Z]{5,10}","I realy like strawberries")) # {5,10} indica um minimo e maximo de repeticoes
# ['realy', 'strawberri']
print(re.findall(r"[a-zA-Z]{5,}","I realy like strawberries")) # {5,} indica um minimo de 5 sem um maximo de repeticoes
# ['realy', 'strawberries']
print(re.findall(r"s\w{,20}","I realy like strawberries")) # {,20} indica um minimo de 0 até 20
# ['strawberries']


# Retorna palavras com no minimo 7 letras
def long_words(text):
  pattern = r"[a-zA-Z]{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []