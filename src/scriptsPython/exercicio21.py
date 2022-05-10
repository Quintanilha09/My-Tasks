nome = str(input('\033[1;34mDigite seu nome completo: \033[m'))
print(nome.title())

if nome.find('Silva') == -1:
    print('\033[1;31mSeu nome não tem Silva.\033[m')
else:
    print('\033[1;32mSeu nome contém Silva.\033[m')
