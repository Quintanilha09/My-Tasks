somaIdades = 0
maiorIdade = 0
menos20Anos = 0

for z in range(1, 5):
    nome = str(input('\033[36mDigite seu nome: '.format(z)))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo:\033[m '))
    somaIdades += idade
    if z == 1 and sexo in 'Mm':
        maiorIdade = idade
        maisVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        maisVelho = nome
    if sexo in 'Ff' and idade < 20:
        menos20Anos += 1

mediaIdades = float(somaIdades / 4)

print('\033[35mA média de idades é\033[m \033[1;33m{:.2f}\033[m'.format(mediaIdades))
print('\033[35mO homem mais velho é\033[m \033[1;36m{}\033[m \033[35mcom\033[m \033[1;36m{} anos\033[m'.format(maisVelho, maiorIdade))
print('\033[1;32m{}\033[m \033[35mmulheres tem menos de \033[1;32m20\033[m \033[35manos\033[m'.format(menos20Anos))

