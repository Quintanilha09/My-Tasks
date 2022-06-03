print('------------\n'
      'CALCULADORA\n'
      '------------')
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
escolha = 0
while escolha != 5:
      print('[1] Somar\n'
            '[2] Multiplicar\n'
            '[3] Maior\n'
            '[4] Novos Números\n'
            '[5] Sair do Programa')
      escolha = int(input('Digite uma opção: '))
      if escolha == 1:
            soma = n1 + n2
            print('{} + {} = {}'.format(n1, n2, soma))
      elif escolha == 2:
            mult = n1 * n2
            print('{} x {} = {}'.format(n1 ,n2, mult))
      elif escolha == 3:
            if n1 > n2:
                  print('{} é maior que {}'.format(n1, n2))
            elif n2 > n1:
                  print('{} é maior que {}'.format(n2, n1))
            elif n1 == n2:
                  print('Não há diferença entre {} e {}'.format(n1, n2))
      elif escolha == 4:
            n1 = int(input('Insira o primeiro número: '))
            n2 = int(input('Insira o segundo número: '))
      elif escolha == 5:
            print('Obrigado')
            break


