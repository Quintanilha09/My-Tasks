import random

print('\033[7;40m-------------------\033[m\n'
      '\033[7;40mJOGO DA ADIVINHAÇÃO\033[m \n'
      '\033[7;40m-------------------\033[m')
print(
    '\033[35mEscolha um número entre\033[35m \033[1;33m1 a \033[1;33m10\033[m \033[35m'
    'e vejamos se você acertará o que a máquina escolheu.\033[m')
num = int(input('\033[35mDigite o número escolhido:\033[m '))
listNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tentativas = 1
escMaquina = random.choice(listNumeros)

while escMaquina != num:
    escMaquina = random.choice(listNumeros)
    if escMaquina != num:
        print('\033[31;40mVocê errou, a máquina escolheu \033[1;36m{}\033[m \033[31;40m.Tente novamente\033[m'.format(
            escMaquina))
        num = int(input('\033[35mDigite o número escolhido:\033[m '))
        tentativas += 1
    elif escMaquina == num:
        print('\033[32;40mVocê venceu, parabéns!. A máquina escolheu\033[m \033[1;33;40m{}\033[m'.format(escMaquina))

print('\033[32;40mVocê atingiu o total de {} tentativas\033[m'.format(tentativas))
