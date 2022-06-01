sal = float(input('\033[1;31;47mInforme seu salário:\033[m '))

salNovo = (15 * sal /100) + sal

print('Seu novo salário aumentou, agora é de \033[7;35m%.2f\033[m ' %salNovo)
