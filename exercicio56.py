print('------------\n'
      '  SUPER PA\n'
      '------------')
termo = int(input('Informe o termo: '))
razao = int(input('Informe a razão: '))
contador = 1
somador = 0
mais = 10
total = 0

while mais != 0:
    total += mais
    while contador <= total:
        contador += 1
        if contador == 2:
            somador += termo
            print('\033[36m', somador, '\033[m', end='\033[1;33m->\033[m')
        somador += razao
        print('\033[36m', somador, '\033[m', end='\033[1;33m->\033[m')
    print('\033[1;30;46mPAUSA\033[m')
    mais = int(input('Quantos termos deseja ter a mais? '))
print('A quantidade de termos mostrado foi de \033[1;36m{}\033[m'.format(total))

















