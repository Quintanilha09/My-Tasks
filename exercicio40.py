valorPag = float(input('Qual é o valor a ser pago pelo produto? '))
print('\033[7;40mQual será a opção de pagamento?\033[m\n'
'\033[32m[1] Dinheiro/Cheque (10% de desconto)\n'
'[2] Cartão (5% de desconto)\n'
'[3] Até 2x no cartão (preço normal)\n'
'[4] 3x ou mais no cartão (20% de juros)\033[m\n')

pagamento = int(input('\033[7;40mInsira aqui uma das opções:\033[m '))

match pagamento:
    case 1:
        valorPag = valorPag - ((10 * valorPag) / 100)
        print('\033[1;33mVocê tem 10% de desconto, o produto saiu por \033[1;34mR${:.2f}\033[m'.format(valorPag))
    case 2:
        valorPag = valorPag - ((5 * valorPag) / 100)
        print('\033[1;33mVocê tem 5% de desconto, o produto saiu por \033[1;34mR${:.2f}\033[m'.format(valorPag))
    case 3:
        print('\033[1;33mNão há descontos para você, o produto saiu por \033[1;34mR${:.2f}\033[m'.format(valorPag))
    case 4:
        valorPag = valorPag + ((20 * valorPag) / 100)
        print('\033[1;33mFoi aplicado 20% de juros para este produto, você terá que pagar \033[1;31mR${:.2f}\033[m'.format(valorPag))
    case _:
        print('Opção não identificada')
