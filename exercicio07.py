largura = float(input('\033[7;40mInforme a largura da parede: \033[m '))
altura = float(input('\033[7;40mInforme a altura da parede:\033[m'))

area = largura * altura

litroTinta = area /2

print('Necessita-se de \033[1;33m%.1f\033[m'%litroTinta, 'litros de tinta para pintar uma area de \033[1;33m%.1f m2\033[m' %area)
