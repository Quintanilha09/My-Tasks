nota1 = float(input('Me informe sua primeira nota: '))
nota2 = float(input('Me informe sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[1;30;41mVocê está reprovado. Estude mais na próxima.\033[m')
elif media >= 5.0 and media <=6.9:
    print('\033[1;30;43mVocê está de recuperação. Ainda existe uma chance.\033[m')
else:
    print('\033[1;30;42mVocê está aprovado. Parabéns pela dedicação.\033[m')
