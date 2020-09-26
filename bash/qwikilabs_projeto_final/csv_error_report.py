import re
import operator
import csv

pattern = r"\bERROR[ \w']*\b"
error_dict = {}

def generate_error_report():
    with open("syslog.log",'r') as file:
        for line in file:
            find=re.search(pattern,line)
            # em versões anteriores do python basta subtituir find[0] por find.group(0)
            if find: # se achar alguma coisa
                if  find.group() in error_dict.keys(): # caso ja adicionado no dict
                    error_dict[find.group()]+=1
                else:
                    error_dict[find.group()]= 1
                    print("key adicionada:"+find.group())

    error_count_list=sorted(error_dict.items(),key=operator.itemgetter(1),reverse=True)
    print (error_count_list) # item getter 0 para ordernar as keys e 1 para os valores

    with open ("error_message.csv","w") as csv_file:
        colunas = ["Error","Count"]
        escrever = csv.writer(csv_file,delimiter=",")
        escrever.writerow(colunas)
        for element in error_count_list:
            escrever.writerow(element)
    print("Error report escrito com sucesso!!")

generate_error_report()