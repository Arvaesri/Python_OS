import re

# termina e comeca com A 
print(re.search(r"^A.*a$","Argentina"))
# <re.Match object; span=(0, 9), match='Argentina'>

# Verificar se é uma nome de variavel valido no python
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$" # no python nao e valido comecar com numeros
print(re.search(pattern,"_this_is_a_valis_variable_name"))
# <re.Match object; span=(0, 30), match='_this_is_a_valis_variable_name'>
print(re.search(pattern,"this isn't a valid variable"))
# None
print(re.search(pattern,"2wrong"))
# None

# Fill in the code to check if the text passed looks like a standard sentence, 
# meaning that it starts with an uppercase letter, followed by at least some lowercase letters 
# or a space, and ends with a period, question mark, or exclamation point.

def verifica_sentenca(text):
    resultado = re.search(r"^[A-Z][\s|a-z]*[\.|\?|\!]$",text)
    return resultado != None

print(verifica_sentenca("Is this is a sentence?")) # True
print(verifica_sentenca("is this is a sentence?")) # False
print(verifica_sentenca("Hello")) # False
print(verifica_sentenca("1-2-3-GO!")) # False
print(verifica_sentenca("A star is born.")) # True

#The check_web_address function checks if the text passed qualifies as a top-level web address, meaning 
# that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well 
# as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such
#  as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters,
#  wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.
def check_web_address(text):
  pattern = r"\w+\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#The check_time function checks for the time format of a 12-hour clock, as follows: the hour is 
# between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then
#  an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to 
# do that. How many of the concepts that you just learned can you use here?
def check_time(text):
  pattern = r"(1[0-2]:|\d:)[0-5][0-9]\s?(am|AM|pm|PM)"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

# The contains_acronym function checks the text for the presence of 2 or more characters or digits
# surrounded by parentheses, with at least the first character in uppercase (if it's a letter), 
# returning True if the condition is met, or False otherwise.
def contains_acronym(text):
  pattern = r"\(([A-Z].+|..+)\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True