velocidade = int(input('\033[4;34mDigite a velocidade do carro:\033[m'))
multa = velocidade - 80
if velocidade > 80:
    print('\033[1;31mVocê foi multado\033[m')
    print('Sua multa é de: \033[1;32m{}\033[m '.format(multa * 7))
else:
    print('\033[1;32mVocê não foi multado\033[m')

