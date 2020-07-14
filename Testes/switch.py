import re
import sys

def switch_name(name):
    pattern = r"^([\w .]*), ([\w .]*)$"
    busca = re.match(pattern,name)
    if busca is None:
        return name
    resultado = "{} {}".format(busca[2],busca[1])
    return resultado