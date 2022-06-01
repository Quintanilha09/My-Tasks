n1 = int(input('\033[35mInsira um número:\033[m '))
n2 = int(input('\033[36mInsira outro número:\033[m '))

if n1 > n2:
    print('\033[1;33m{}\033[34m é maior\033[m'.format(n1))
elif n2 > n1:
    print('\033[1;33m{} \033[34mé maior\033[m '.format(n2))
else:
    print('\033[7;40mOs dois números são iguais\033[m')