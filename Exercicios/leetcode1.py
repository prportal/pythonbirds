def two_sum(target, *args):
    """Esta função retorna os índices dos elementos cujas a soma
    são -é igual ao valor do parametro target
    args é uma tupla com o elementos a serem pesquisados
    target é o valor a ser encontrado
    pos_a é o valor do índice da primeira posição que será somada
    pos_b1 é a posição do segundo valor que esta sendo somado
    pos_b é a posição da tupla onde deve começar a pesquisa do segundo valor    """
    pos_a=0
    pos_b=1
    pos_b1=1
    for um in args:
        pos_b1 = pos_b
        for outro in args[pos_b:]:
            if target==um+outro:
                return(pos_a, pos_b1)
            pos_b1+=1
        pos_a+=1
        pos_b+=1
#
print(two_sum(12, 3, 5, 9, 15, 18, 20))
