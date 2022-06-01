sexo = str(input('Qual é o seu sexo? [F] ou [M]')).upper()

while sexo not in 'FfMm':
    print('Valor inválido, tente novamente.')
    sexo = str(input('Qual é o seu sexo? [M] ou [F]')).upper()
print('Obrigado por informar')