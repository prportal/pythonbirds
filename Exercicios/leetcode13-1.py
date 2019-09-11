_rom_int = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL': 40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1,}
def define_val_elem_anterior(roman_str):
    tam_x = len(roman_str)
    valor = 0
    if tam_x <= 0:
        return (1999) # soh para retornar um valor válido na ultima execução

    elemento_x = roman_str[tam_x - 2: tam_x]
    elemento_x1 = roman_str[tam_x - 1:tam_x]
    if elemento_x in _rom_int:
        valor = (_rom_int[elemento_x])
    elif elemento_x1 in _rom_int:
        valor = (_rom_int[elemento_x1])
    else:
        valor = 9999999
#
    return(valor)

def valida_string_romano(roman_string):
    print (roman_string)
    tam = len(roman_string)
    if tam <= 0:
        return(True)
    #
    if 'MMMM' in roman_string or 'CCCC' in roman_string or 'XXXX' in roman_string or 'IIII' in roman_string:
        return(False)
    if 'DD' in roman_string or 'LL' in roman_string or 'VV' in roman_string:
        return(False)
    #
    elemento = roman_string[tam - 2: tam]
    elemento_1 = roman_string[tam - 1]
    if elemento in _rom_int:
        roman_string = roman_string[0:tam - 2]
        valor_atual = _rom_int[elemento]
    elif elemento_1 in _rom_int:
        roman_string = roman_string[0:tam - 1]
        valor_atual = _rom_int[elemento_1]
    else:
        return (False)
    valor_anterior = define_val_elem_anterior(roman_string)
    if valor_anterior != valor_atual:
        diferenca = valor_anterior - valor_atual
        if diferenca in (1, 4, 8, 10, 40, 80, 100, 400, 800):
            return(False)

    if valor_anterior < valor_atual:
        return(False)
    return(valida_string_romano(roman_string))

romano = 'MMMCCXLIX'
e_valido = valida_string_romano(romano)
if e_valido:
    print(romano, '    ', 'é número romano')
else:
    print(romano, '   Nao eh um numero romano')

