maior = 0
menor = 0
for j in range(1, 6, 1):
    peso = float(input('Informe o {}° peso: '.format(j)))
    if j == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {}\n'
      'O menor peso é {}'.format(maior, menor))
