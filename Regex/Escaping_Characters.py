import re

# \ Escape character , vai permitir o uso dos caracteres especiais[^$.?+*] na busca de match )
# \w (match em qualquer caractere alfanumerico)
# \W Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]. 
# \d (match em digitos)
# \s (match em caracteres de espaco branco[space,tab,newline...])
# \S Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
# \b (match em word boundaries)

print(re.search(r".com","welcome"))
# <re.Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com",".com"))
# <re.Match object; span=(0, 4), match='.com'>

print(re.search(r"\w*","This is an exemple")) # backspace nao conta como alfanumerico
# <re.Match object; span=(0, 4), match='This'>
print(re.search(r"\w*","This_is_another"))
# <re.Match object; span=(0, 15), match='This_is_another'>


# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters 
# (including letters, numbers, and underscores) separated by one or more whitespace characters.
def check_grupo(text):
    resultado = re.search(r"\w\w+\s+",text)
    return resultado != None

print(check_grupo("One")) # False
print(check_grupo("123  Ready Set GO")) # True
print(check_grupo("username user_01")) # True
print(check_grupo("shopping_list: milk, bread, eggs.")) # False