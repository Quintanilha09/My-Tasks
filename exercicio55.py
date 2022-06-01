print('-------------\n'
      'GERADOR DE PA\n'
      '-------------')
contador = 1
somador = 0
termo = int(input('Qual é o primeiro termo? '))
razao = int(input('Qual é a razão? '))
while contador <= 9:
    contador += 1
    if contador == 2:
        somador += termo
        print(somador, end='->')
    somador += razao
    print(somador, end='->')
print('FIM')
