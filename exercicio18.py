nome = str(input('\033[34mDigite seu nome completo:\033[m ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' ')) #estou pedindo para contar as letras do nome completo e subtrair os espaços
print('Seu primeiro nome tem \033[32m{}\033[m letras'.format(nome.find(' ')))
lista = nome.split()
print('\033[35m', lista, '\033[m')


