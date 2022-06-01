import math
n = float(input('\033[32mDigite um número real:\033[m '))

inteiro = math.ceil(n)

print('\033[7;40mO número {} inteiro seria \033[1;33m{}\033[m \033[m'.format(n,inteiro))