import random

num = random.randint(0,5)
escolha = int(input('\033[1;36mQual número você acha que a máquina escolheu?\033[m '))

if escolha == num:
    print('\033[33mParabéns, você acertou!\033[m')
else:
    print('\033[31mDroga, não foi dessa vez.\033[m')

print('A máquina escolheu: \033[32m{}\033[m'.format(num))