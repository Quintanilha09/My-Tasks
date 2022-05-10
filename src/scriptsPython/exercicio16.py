import random

aluno1 = input('\033[30;46mNome do aluno: ')
aluno2 = input('Nome do aluno: ')
aluno3 = input('Nome do aluno: ')
aluno4 = input('Nome do aluno: \033[m')

lista = [aluno1,aluno2,aluno3,aluno4]

random.shuffle(lista)

print('\033[1;33m',lista, '\033[m')