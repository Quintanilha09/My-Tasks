import random

aluno1 = input('\033[34mDigite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno:\033[m ')

lista = [aluno1,aluno2,aluno3,aluno4]

sorteio = random.choice(lista)

print('O aluno sorteado é: ', '\033[1;33m',sorteio,'\033[m')
