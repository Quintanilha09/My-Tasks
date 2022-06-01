num = int(input('\033[33mDigite um número inteiro:\033[m '))
base = int(input('\033[33mQual será a base de conversão [1]binário [2]octal? [3]hexadecimal: \033[m '))

if base == 1:
    conversao = bin(num)
    print('\033[34mA conversão de \033[1;32m{}\033[m \033[34mpara binário é\033[m \033[1;32m{}\033[m'.format(num, conversao))
elif base ==2:
    conversao = oct(num)
    print('\033[34mA conversão de \033[1;32m{}\033[m \033[34mpara octal é\033[m \033[1;32m{}\033[m'.format(num, conversao))
elif base ==3:
    conversao = hex(num)
    print('\033[34mA conversão de \033[1;32m{}\033[m \033[34mpara hexadecimal é\033[m \033[1;32m{}\033[m'.format(num, conversao))