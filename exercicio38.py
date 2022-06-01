reta1 = float(input('\033[1;34mInforme a primeira reta: \033[m'))
reta2 = float(input('\033[1;34mInforme a segunda reta: \033[m'))
reta3 = float(input('\033[1;34mInforme a terceira reta: \033[m'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\033[1;32mÉ possível montar um triângulo\033[m', end='')
    if reta1 == reta2 == reta3:
        print(' \033[1;33mEquilátero\033[m')
    if reta2 == reta3 or reta1 == reta2:
        print(' \033[1;33mIsósceles\033[m')
    if reta1 != reta2 != reta3:
        print(' \033[1;33mEscaleno\033[m')
else:
    print('\033[1;31mNão é possível montar um triângulo\033[m')