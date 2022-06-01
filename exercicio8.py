preco = float(input('\033[4;37mInforme o preço do produto:\033[m '))

novoPreco= (5 * preco /100) + preco

print('O produto foi atualizado, agora está valendo \033[33mR$ %.2f\033[m' %novoPreco)