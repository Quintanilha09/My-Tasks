frase = str(input('Digite uma frase:').strip().lower())
separacao = frase.split()
juncao = ''.join(separacao)
inversao = ''
# inversao = juncao[::-1] eu poderia ter feito dessa forma sem usar o for

for contl in range(len(juncao) - 1, -1, -1):
    inversao += juncao[contl]
if inversao == juncao:
    print('\033[33mÉ um palíndromo\033[m')
else:
    print('\033[33mNão é um palíndromo\033[m')

print('{}\n{}'.format(juncao, inversao))

















print(len(frase))