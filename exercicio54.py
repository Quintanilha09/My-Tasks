n = int(input('Digite um número: '))
contador = n
fatorial = 1
print('{}! = '.format(n),end='')
while contador > 0:
    print('{}'.format(contador),end='')
    print(' x ' if contador > 1 else ' = ',end='')
    fatorial *= contador
    contador -= 1
print(fatorial)