print('\n-------------------'
      'SEQUÊNCIA FIBONACCI'
      '-------------------\n')
termo = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
contador = 3
soma = 0
print('{}-> {}'.format(termo1, termo2), end='->')
while contador < termo:
    contador += 1
    soma = termo1 + termo2
    termo1 = termo2
    termo2 = soma
    print(' {}'.format(soma), end='->')
print('FIM')











