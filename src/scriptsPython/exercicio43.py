for cont in range(1,50,1):
    if cont % 2 == 0:
        print('\033[1;33m' ,cont, '\033[m', '\033[34mPar\033[m ')
    else:
        print('\033[1;35m', cont, '\033[m' '\033[31mImpar\033[m ')