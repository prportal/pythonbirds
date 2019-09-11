def verifica_pref(str_1, str_2):
    ## Esta função verificaa a qtd de caracteres
    ## iguais no início de 2 strings
    ## retorna a qtd de caracteres iguais
    tam_pref = 0
    pos_str = 0
    if len(str_1) >= len(str_2):
        tam_str = len(str_2)
    else:
        tam_str = len(str_1)
    while pos_str < tam_str:
        if str_1[pos_str] == str_2[pos_str]:
            tam_pref += 1
            pos_str += 1
        else:
            pos_str = tam_str
    return(tam_pref)
#
#
#
def maior_prefixo(lista_base, pos):
    ## Esta função verifica a maior sequencia de caracteres iguais
    ## no início dos strings que compõe a lista_base
    ## retorna a maior sequência encontrada
    if len(lista_base) == 0:
        return('Lista vazia')
    if len(lista_base) == 1:
        return(max(lista_result))
    lista_base.sort()
    print(lista_base)
    string_1 = lista_base[0]
    string_2 = lista_base[1]
    strngx = lista_base.pop(0)
    print(strngx)
    pos += 1
    tamx = verifica_pref(string_1, string_2)
    lista_result.append(tamx)
    return(maior_prefixo(lista_base, pos))
##
##
##
lista_result = [0]
pos = 0
lista = ['joao', 'jose', 'jairone', 'ary', 'aryan', 'jairo']
## lista = ['j', 'ka', 'p', '', 'b', 'c']
## lista =[]
print(maior_prefixo(lista, pos))
