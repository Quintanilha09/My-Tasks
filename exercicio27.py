distancia = int(input('\033[7;40mQual é a distância da viagem em km?\033[m '))
preco = float(0)

if distancia <=200:
    preco = 0.50 * distancia
    print('\033[4;30;41m preço da passagem fica por\033[m \033[1;33mR${:.2f}\033[m'.format(preco))
else:
    preco = 0.45 * distancia
    print('\033[4;30;41mO preço da passagem fica por\033[1;33mR${:.2f}\033[m'.format(preco))