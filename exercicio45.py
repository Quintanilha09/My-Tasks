print('PROGREÇÃO ARITMÉTICA\n')
pTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Agora digite a razão'))
soma = 0

for cont in range(pTermo,10,razao):
    soma = soma + razao
    print(soma)
        