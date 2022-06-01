num = int(input('\033[32mDigite um número:\033[m '))
somador = 0
for cont in range(1, num, 1):
    if num % cont == 0 and num % num == 0:
       somador = somador + 1

if somador <= 2:
    print('{} \033[1;34mé primo\033[m'.format(num))
elif somador > 2:
    print('{} \033[1;36mnão é primo\033[m'.format(num))
