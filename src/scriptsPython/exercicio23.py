nome = str(input('\033[7;37mDigite seu nome completo: \033[m '))
n = nome.split()

print('Primeiro nome: \033[1;33m{}\033[m'.format(n[0]))
print('Último nome: \033[1;33m{}\033[m'.format(n[len(n)-1])) #eu pedi para que a maquina analisar quantas listas tem e pegar a última,
# porque sempre vai dar um numero a mais, por isso o -1

