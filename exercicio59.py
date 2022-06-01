n = 0
resposta = 's'
somador = 0
contador = 0
menorNum = 0
maiorNum = 0
while resposta == 's':
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [s] ou [n]:')).lower()
    somador += n
    contador += 1
    if contador == 1:
        menorNum = n
        maiorNum = n
    if n < menorNum:
        menorNum = n
    if n > maiorNum:
        maiorNum = n

media = float(somador / contador)
print('A média de todos os números é: {}\n'
      'O menor número é: {}\n'
      'O maior número é: {}'.format(media, menorNum, maiorNum))






