n1 = int(input('\033[7;40mInsira um número:\033[m '))
n2 = int(input('\033[7;40mInsira outro número:\033[m '))
n3 = int(input('\033[7;40mInsira outro número:\033[m '))

if n1 > n2 and n3:
    print('\033[34m{}\033[m \033[1;36mé o maior\033[m'.format(n1))
elif n2 > n3:
    print('\033[34m{}\033[m \033[1;36mé o maior\033[m'.format(n2))
elif n3 > n1:
    print('\033[34m{}\033[m \033[1;36mé o maior\033[m'.format(n3))