quantidadeKm = float(input('\033[4;34mQuantos km foram percorridos? '))
dias = int(input('Por quantos dias foi alugado? \033[m'))

precokm = 0.15 * quantidadeKm
precoDias = 60 * dias

print('Você terá que pagar \033[1;31mR$ %.2f\033[m '%precokm,' por ter rodado %.1f'%quantidadeKm,'km \nE também \033[1;31mR$ %.2f\033[m' %precoDias,' pelos', dias,' dias')