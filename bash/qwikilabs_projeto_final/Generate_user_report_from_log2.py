#!/usr/bin/env python3
import operator
import re
import csv

pattern  = r"(\b[INFO|ERROR][\w ']*\b) [\[\]#\d ]*\(([\w \.]*)\)"
dict_user_error ={}
dict_user_info={}

def generate_dictionary_from_log():
        with open("syslog.log","r") as log:
                for line in log:
                        match=re.search(pattern,line)
                        if match:
                                if "INFO" in match.group(1):
                                        if match.group(2) in dict_user_info.keys():
                                                dict_user_info[match.group(2)]+=1
                                        else:
                                                dict_user_info[match.group(2)]=1
                                if "ERROR" in match.group(1):
                                        if match.group(2) in dict_user_error.keys():
                                                dict_user_error[match.group(2)]+=1
                                        else:
                                                dict_user_error[match.group(2)]=1


def create_user_list_from_dict():
        user_list = []
        for user in dict_user_info.keys():
                user_list.append(user)
        for user in dict_user_error.keys():
                if user not in user_list:
                        user_list.append(user)
        user_list.sort()
        return user_list

def verifica_dicionario_sem_usuario(dict_user_info,dict_user_error,user_list):
        for user in user_list:
                if user not in dict_user_info.keys():
                        dict_user_info[user]=0
                if user not in dict_user_error.keys():
                        dict_user_error[user]=0

def generate_csv(user_list):
        with open("user_statistics.csv","w")as user_csv:
                csv_handler = csv.writer(user_csv)
                csv_handler.writerow(["Username","INFO","ERROR"])
                for i,user in enumerate(user_list): # tentar gravar apenas os 5 primeiros
                        csv_handler.writerow([user,dict_user_info[user],dict_user_error[user]])
                        if i == 7:
                                break
                print("Report OK")

def main():
        generate_dictionary_from_log()
        user_list = create_user_list_from_dict()
        print(user_list)
        verifica_dicionario_sem_usuario(dict_user_info,dict_user_error,user_list)
        generate_csv(user_list)

main()