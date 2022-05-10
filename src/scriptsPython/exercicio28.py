ano = int(input('\033[1;36mInsira uma data:\033[m '))

if ano % 4 == 0:
    print('\033[4;32m{}\033[m \033[1;33mé um ano bissexto\033[m'.format(ano))
else:
    print('\033[4;32m{}\033[m \033[1;33mnão é um ano bissexto \033[m'.format(ano))