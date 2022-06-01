idade = int(input('Informe sua idade: '))

if idade < 18:
    tempoFaltante = 18 - idade
    print('\033[1;32;40mSorte sua, ainda não é hora de se alistar no exército.\033[m')
    print('\033[1;32;40mAinda faltam {} anos para você\033[m'.format(tempoFaltante))
elif idade == 18:
    print('\033[1;30;42mJá está na hora de se alistar.\033[m')
else:
    tempoFaltente = idade - 18
    print('\033[1;30;41mPassou do tempo de alistamento.\033[m \n')
    print('\033[1;30;41mVocê ultrapassou {} anos do tempo de alistamento\033[m'.format(tempoFaltente))
    print('\033[1;31mTOMA CUIDADO!\033[m')