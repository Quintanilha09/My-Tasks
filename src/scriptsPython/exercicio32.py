print('SEU EMPRÉSTIMO')

valorCasa = float(input('\033[36mInsira o valor da casa: '))
salComprador= float(input('Insira seu salário: '))
anosPag = int(input('Em quantos anos pretende pagar?\033[m'))

parcelas = float(valorCasa / anosPag)

if parcelas <= (30 * salComprador) /100:
    print('\033[1;33;40mSeu empréstimo foi aprovado, você terá que pagar \033[1;32mR${:.2f}\033[m\033[m'.format(parcelas))
else:
    print('\033[1;31mVocê não pode comprar esta casa, pois não tem saldo o suficiente para as parcelas. Que ficarão por \033[1;33mR${:.2f}\033[m\033[m'.format(parcelas))

