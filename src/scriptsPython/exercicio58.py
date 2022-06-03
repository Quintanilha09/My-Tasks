n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    print(soma)
    cont += 1
    soma += n
print('Foram digitados {} números\n'
      'A soma de todos os números digitados é: {}'.format(cont - 1, soma - 999))