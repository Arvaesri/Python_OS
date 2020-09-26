import csv
with open("profissoes.csv", "w") as arquivo_csv:
    colunas = ["nome", "profissao"]
    escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=",", lineterminator="\n")
    escrever.writeheader()
    escrever.writerow({"nome": "Renato", "profissao": "programador"})
    escrever.writerow({"nome": "Yanka", "profissao": "programadora"})


with open("profissoes.csv", "r") as arquivo_csv:
    reader_iterable_object = list(csv.reader(arquivo_csv)) # lista contendo outra lista com as linhas co csv
    print(reader_iterable_object)
    for element in reader_iterable_object:
        print (element)
        # ['nome', 'profissao']
        # ['Renato', 'programador']
        # 'Yanka', 'programadora']