sal = float(input('\033[7;40mInforme seu salário R$:\033[m '))
aumento = float(0)

if sal > 1250:
    aumento = (10 * sal) / 100
    print('\033[1;36;40mSeu salário agora é de \033[1;32mR${:.2f}\033[m\033[m'.format(sal + aumento))
else:
    aumento = (15 * sal) / 100
    print('\033[1;36;40mSeu salário agora é de \033[1;32mR${:.2f}\033[m\033[m'.format(sal + aumento))
