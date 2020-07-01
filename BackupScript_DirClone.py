import os

# Script Para Fazer Backup dos saves e copia dos diretorios(nao recursivo por enquanto)

path_arquivo = "D:\\Users\\arthu\\Documents\\Criterion Games\\Need For Speed(TM) Most Wanted\\Save\\2503770513"
path_backup = "D:\\Users\\arthu\\Desktop\\NFS-Most Wanted save Backup\\Save\\2503770513"

def atualizar_arquivo(caminho_arquivo,caminho_backup):

    with open(caminho_arquivo,"rb") as arquivo_atualizado:  # read e write em binary para n dar erro
        copia_atualizada = arquivo_atualizado.read()

    with open(caminho_backup ,"wb") as arquivo_backup: 
        arquivo_backup.write(copia_atualizada)



def atualizar_diretorio(diretorio_arquivo,diretorio_backup):
    lista_backup = os.listdir(diretorio_backup)
    lista_arquivo = os.listdir(diretorio_arquivo)
    if lista_backup != lista_arquivo:
        print("\nLISTA DE ARQUIVOS DIFERENTES !!!\n")
    
    for x in lista_arquivo: # A pasta que vai ser iterada deve ser a do save já que não importa os arquivos do backup
        atualizar_arquivo(path_arquivo + "\\" + x ,path_backup + "\\" + x)



atualizar_diretorio(path_arquivo,path_backup)

