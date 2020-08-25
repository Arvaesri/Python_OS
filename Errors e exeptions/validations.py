def validate_user(username,minlen):
    assert type(username) == str,"Usuario deve ser uma string" # Assert auxilia a descobrir o motivo do erro ter ocorrido, vai gerar um assert error caso a condicao seja falsa
    if minlen < 1:                                              
        raise ValueError("Minlen deve ser no minimo 1") # raise gera um erro do tipo passado e uma mensagem
    if  len(username) < minlen:
        return False
    if not username.isalnum(): # letras e numeros
        return False

    return True

# username = input("Username:") # input vai retornar uma string ,para ver a mensagem do assert é necessario passar o valor diretamente
# minlen = input("minlen:")
# print(validate_user(username,int(minlen)))