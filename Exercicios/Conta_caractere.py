def conta_caractere(s):
    print('String', '=', s)
    caracteres_ordenados = sorted(s)
    caractere_anterior = caracteres_ordenados[0]
    contagem = 1
    total = 1
    espaço = '           '
    print('Caractere', '  ', 'Qtd')
    for caractere in caracteres_ordenados[1:]:
        if caractere_anterior != ' ':
            if caractere==caractere_anterior:
                total += 1
                contagem+=1
            else:
                print(f'{caractere_anterior} {espaço} {contagem}')
                caractere_anterior = caractere
                total += 1
                contagem = 1
        else:
            caractere_anterior = caractere
    print(f'{caractere_anterior} {espaço} {contagem}')
    print('Total  ', total)

conta_caractere('Gremio tri campeao da america')
print('   ')
conta_caractere('Meu nome é Paulo')
