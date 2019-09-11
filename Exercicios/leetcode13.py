_rom_int = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}

def converte_rom_int(roman_string):
    print (roman_string)
    tam = len(roman_string)
    inteiro = 0
    if tam > 0:
      elemento = roman_string[tam - 2: tam]
      if elemento in _rom_int:
          inteiro += _rom_int[elemento]
          roman_string = roman_string[0:tam - 2]
      else:
          elemento = roman_string[tam - 1]
          if elemento in _rom_int:
              inteiro += _rom_int[elemento]
              roman_string = roman_string[0:tam - 1]
          else:
              return (9999999)
      inteiro += converte_rom_int(roman_string)
    return(inteiro)

romano = 'MMMCCCXLIX'
inteiro = converte_rom_int(romano)
if inteiro == 9999999:
    print(romano, '   Nao eh um numero romano')
else:
    print(romano, '    ', inteiro)
