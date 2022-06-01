n = int(input('\033[35mDigite um número:\033[m '))
cont = 0

while cont <10:
    cont = cont + 1
    result = n * cont
    print('\033[1;33m{}\033[m X \033[1;31m{}\033[m = \033[1;34m{}\033[m'.format(n, cont, result))