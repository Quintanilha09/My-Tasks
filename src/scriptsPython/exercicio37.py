idade = int(input('\033[34mInforme sua idade:\033[m '))

if idade <=9:
    print('Sua categoria é \033[33mMirim\033[m')
elif idade <=14:
    print('Sua categoria é \033[33mInfantil\033[m')
elif idade <=19:
    print('Sua categoria é \033[33mJunior\033[m')
elif idade ==20:
    print('Sua categoria é \033[33mSênior\033[m')
else:
    print('Sua categoria é \033[33mMaster\033[m')

