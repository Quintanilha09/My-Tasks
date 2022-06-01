n = int(input('\033[7;40mDigite um número:\033[m '))

print('O número {} tem:'.format(n))
print('Unidade: {}'.format(n[-1]))
print('Dezena: {}'.format(n[-2]))
print('Centena: {}'.format(n[-3]))
print('Milhar {}'.format(n[0]))
