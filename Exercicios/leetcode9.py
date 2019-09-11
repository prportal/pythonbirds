def reverso(x):
    #
    rev = 0
    while x >= 1:
       # operação pop
       pop = x % 10
       x /= 10
       x = int(x)
       # operação push
       rev = rev * 10 + pop
    return (rev)
##
def palindrome(numero):
   # if numero < 0:
   #     return(numero, 'não é palindromo')
   # if numero == reverso(numero):
   #     return(numero, 'é palindromo')
   # else:
   #     return(numero, 'não é palindromo')

    if str(numero) == str(numero)[::-1]:
        return(numero, 'é palindromo')
    else:
        return(numero, 'não é palindromo')
#
print(palindrome(1233321))
