
while(True):
    from random import randint
    from time import sleep
    #meu objetivo é criar dois jogadores, um que será usuário e outro que será o pc
    #crio uma lista com as jogadas
    lis=['Pedra','Papel','Tesoura']
    a=randint(0,len(lis)-1)
    print("""Faça sua jogada no Jô-Ken-Pô:
    [0] Pedra
    [1] Papel
    [2] Tesoura:""")
    jog=int(input('jogada: '))
    if (jog>=0 and jog<=2):
        jogador=lis[jog]
        pc=lis[a]
        print('Jô')
        sleep(0.5)
        print('Ken')
        sleep(0.5)
        print('Pô')
        sleep(0.5)
        if (jog==a):
            print("Vixee, empatou...")
        elif ((jog==0 and a==2) or (jog==2 and a==1) or (jog==1 and a==0)):
            print("Você venceu!")    
        else:
            print("PC venceu")
        print("Você escolheu {} e o pc escolheu {}". format(jogador,pc))
    elif (jog>2 or jog<0):
        print('Jogada invalida, tente novamente')        
    opc=input('Quer continuar? [s para sim/n para não] ').lower().strip()
    if opc=='n':
        break