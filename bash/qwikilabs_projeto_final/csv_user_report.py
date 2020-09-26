import csv
import re
import operator

pattern_user = r"([INFO|ERROR][\w ]*)[\[\] \d#]*\(([\w ]*)\)"

dict_user_error = {}
dict_user_info = {}
user_list=[]

def generate_dictionary_from_log(dict_user_info,dict_user_error):
    with open ("syslog.log","r") as log:
        for line in log:
            match=re.search(pattern_user,line)
            if match: # diferente de NONE
                if "INFO" in match[1]:
                    if match[2] in dict_user_info.keys(): # caso o usuario ja esteja no dicionario
                        dict_user_info[match[2]]+=1
                    else:
                        dict_user_info[match[2]] = 1 # primeira vez
                        print(match[2] +" adicionado ao dicionario de info")
                if "ERROR" in match[1]:
                    if match[2] in dict_user_error.keys(): # caso o usuario ja esteja no dicionario
                        dict_user_error[match[2]]+=1
                    else:
                        dict_user_error[match[2]] = 1 # primeira vez
                        print(match[2] +" adicionado ao dicionario de errors")

# generate_dictionary_from_log(dict_user_info,dict_user_error)

def create_user_list():
    for user in dict_user_info.keys(): # criando uma lista com o nome de todos os usuarios aprtir dos dicionarios
        user_list.append(user)
    for user in dict_user_error.keys():
        if user not in user_list: # caso os usuarios do segundo dicionario nao estejam na lista
            user_list.append(user)
    user_list.sort()
    return user_list

# user_list = create_user_list()

def verifica_dicionario_sem_usuario(dict_user_info,dict_user_error,user_list):
    for user in user_list: # percorendo todos os usuarios e verificando nos 2 dicionarios quais valores são 0
        if user not in dict_user_info.keys():
            dict_user_info[user] = 0
        if user not in dict_user_error.keys():
            dict_user_error[user] = 0

# verifica_dicionario_sem_usuario(dict_user_info,dict_user_error,user_list)

def generate_csv():
    with open ("user_statistics.csv","w") as user_csv:
        csv_handler = csv.writer(user_csv,delimiter=",")
        csv_handler.writerow(["Username","INFO","ERROR"])
        for user in user_list:
            csv_handler.writerow([user,dict_user_info[user],dict_user_error[user]])
    print("User statistics report escrito com sucesso !!")

def main():
    generate_dictionary_from_log(dict_user_info,dict_user_error)
    create_user_list()
    print("\n"+"Lista de todos os usuarios:")
    print(user_list)
    verifica_dicionario_sem_usuario(dict_user_info,dict_user_error,user_list)
    generate_csv()

main()
# if __name__=="__main__": # se o nome do modulo for main , ou seja so vai executar se o programa for executado por si só , e não no import
#     print("variavel __name__ = "+ __name__)
#     main()