maiores = 0
menores = 0
for c in range(0,7,1):
    nasc = int(input('Informe o ano de nascimento'))
    if 2022 - nasc >= 18:
        maiores += 1
    else:
        menores += 1

print('\033[1;36m{}\033[m \033[35mpessoas já atingiram a maioridade\033[m\n'
      '\033[1;33m{}\033[m \033[35mainda são menores\033[m'.format(maiores, menores))