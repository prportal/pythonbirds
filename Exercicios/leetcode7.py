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
##
print(reverso(1221))
