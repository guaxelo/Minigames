from time import sleep
from random import randint

def jogos():
    pensamento()
    jokenpo()
def pensamento():
    print('')
    linhas()
    print('    LEIA SE FOR CAPAZ')

    numpcadv = randint(0, 100)
    vidasadv = 5
    while vidasadv > 0:
        linhas()
        print(f'VIDAS RESTANTES: {vidasadv}\n')
        numjogadoradv = int(input('>> QUAL NUMERO ESTOU PENSANDO? '))
        linhas()
        if numpcadv == numjogadoradv:
            sleep(1)
            print('>>>> JOGADOR GANHOU!')
            break
        else:
            if numjogadoradv > numpcadv:
                sleep(1)
                print('>> ESCOLHA UM NUMERO MENOR!')
                vidasadv -= 1

            else:
                sleep(1)
                print('>> ESCOLHA UM NUMERO MAIOR!')
                vidasadv -= 1

    if vidasadv == 0:
        sleep(2)
        print('VOCE PERDEU! :/')
        print(f'O NUMERO ESCOLHIDO PELO COMPUTADOR FOI: {numpcadv}')
    else:
        sleep(1)
        print(f'SOBRARAM {vidasadv} VIDAS')
def jokenpo():
        # 1 - Pedra/ 2 - Papel / 3 - Tesoura
        op = ['PE', 'PA', 'TE']
        linhas()
        print('         JOKENPÔ')
        linhas()
        print('>> PE - PEDRA\n>> PA - PAPEL\n>> TE - TESOURA')
        vidasjpk = 3
        recordejpk = 0
        while True:
            numpcjpk = randint(1, 3)
            if numpcjpk == 1:
                escpcjkp = 'PEDRA'
            elif numpcjpk == 2:
                escpcjkp = 'PAPEL'
            else:
                escpcjkp = 'TESOURA'
            while True:
                linhas()
                print(f'RECORDE ATUAL: {recordejpk}')
                print(f"VIDAS RESTANTE: {vidasjpk} ")
                jogadorjpk = str(input('\nESCOLHA SUA OPÇÃO: ')).upper()[0:2]

                if jogadorjpk not in op:
                    linhas()
                    print('OPÇÃO INVALIDA ESCOLHA ENTRE PA, PE e TE')
                else:
                    if jogadorjpk == 'PE':
                        numjogadorjpk = 1
                        sleep(1)
                        print('>> JOGADOR ESCOLHE PEDRA')
                        break
                    elif jogadorjpk == 'PA':
                        numjogadorjpk = 2
                        sleep(1)
                        print('>> JOGADOR ESCOLHE PAPEL')
                        break
                    else:
                        sleep(1)
                        numjogadorjpk = 3
                        print('>> JOGADOR ESCOLHE TESOURA')
                        break
            sleep(1)
            print(f'>> PC ESCOLHE {escpcjkp}')
            sleep(2)
            if numpcjpk != numjogadorjpk:
                if numjogadorjpk == 1 and numpcjpk == 3 or numjogadorjpk == 3 and numpcjpk == 2 or numjogadorjpk == 2 and numpcjpk == 1:
                    linhas()
                    print('\n===> JOGADOR VENCEU\n')
                    recordejpk += 1

                else:
                    linhas()
                    print('\n===> PC VENCEU\n')
                    vidasjpk -= 1
            else:
                linhas()
                print('\nEMPATE... ESCOLHA NOVAMENTE\n')
            if vidasjpk == 0:
                linhas()
                print('\nFIM DE JOGO')
                print(f'SEU RECORDE FOI: {recordejpk}\n')
                linhas()
                break
def linhas():
    print('=========================')


linhas()
print("""JOGOS DISPONIVEIS

1 - JOKEPÔ
2 - ADVINHAÇÃO
""")

opcoesdejogo = ['1', '2']
jogo = ''
while True:
    linhas()
    jogo = str(input('ESCOLHA SUA OPÇÃO: '))

    if jogo not in opcoesdejogo:
        linhas()
        print("""OPÇÃO INVALIDA ESCOLHA ENTRE:
        
1 - JOKEPÔ
2 - ADVINHAÇÃO""")
    else:
        if jogo == '1':
            sleep(2)
            jokenpo()
        else:
            sleep(2)
            pensamento()


