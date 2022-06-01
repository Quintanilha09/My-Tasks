num = int(input('\033[7;40mDigite um número: \033[m'))

if num % 2 == 0:
    print('\033[7;40m{}\033[m é par'.format(num))
else:
    print('\033[7;40m{}\033[m é impar'.format(num))