metro = int(input('\033[7;40mQuantos metros deseja converter? \033[m'))

centimetro = metro * 100
milimetro = metro * 1000

print('\033[4;31m{}\033[m metros é o mesmo que \033[4;31m{} centimetros\033[m e \033[4;31m{} milimetros \033[m'.format(metro,centimetro,milimetro))