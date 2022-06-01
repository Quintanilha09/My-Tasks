peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 > imc <= 25:
    print('Você está no peso ideal.')
elif 25 > imc <= 30:
    print('Você está em sobrepeso, toma cuidado!')
elif 30 > imc <= 40:
    print('Você é obeso, faça academia.')
else:
    print('Você tem obesidade mórbida, está com o pé na cova.')
