def conta_caractere(s):
    caracteres_ordenados = sorted(s)
    caractere_anterior = caracteres_ordenados[0]
    contagem = 1
    resultado={}
    for caractere in caracteres_ordenados[1:]:
        if caractere_anterior != ' ':
            if caractere==caractere_anterior:
                contagem+=1
            else:
                resultado[caractere_anterior] = contagem
                caractere_anterior = caractere
                contagem = 1
        else:
            caractere_anterior = caractere
    resultado[caractere_anterior] = contagem
    return (resultado)

print(conta_caractere('Gremio tri campeao da america'))

print('   ')
print(conta_caractere('Meu nome é Paulo'))
